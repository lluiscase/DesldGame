import pygame
import defaults
import random
import time
import math
from OpenGL.GL import *
from OpenGL.GLU import *
import opengl as ogl

enemies_list = []
start = time.time()
interval = 2.0
screen_distortion_effect = False
distortion_start = 0

trash_types = ["organico", "vidro", "plastico", "metal"]
trash_images = {
    "organico": "./img/trash.png",
    "vidro": "./img/trash.png",
    "plastico": "./img/trash.png",
    "metal": "./img/trash.png"
}

box_image_path = "./img/trash.png"

# Globals OpenGL
_gl_inited = False
_shader_programs = {}
_texture_map = {}
_box_texture = None
_window_size = (defaults.WINDOW_WIDTH, defaults.WINDOW_HEIGHT)

def create_shader_program(vertex_src, fragment_src):
    v = glCreateShader(GL_VERTEX_SHADER)
    f = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(v, vertex_src)
    glShaderSource(f, fragment_src)
    glCompileShader(v)
    if not glGetShaderiv(v, GL_COMPILE_STATUS):
        raise RuntimeError(glGetShaderInfoLog(v).decode())
    glCompileShader(f)
    if not glGetShaderiv(f, GL_COMPILE_STATUS):
        raise RuntimeError(glGetShaderInfoLog(f).decode())
    p = glCreateProgram()
    glAttachShader(p, v)
    glAttachShader(p, f)
    glLinkProgram(p)
    if not glGetProgramiv(p, GL_LINK_STATUS):
        raise RuntimeError(glGetProgramInfoLog(p).decode())
    # cleanup shaders
    glDeleteShader(v)
    glDeleteShader(f)
    return p

def surface_to_texture(surface):
    surface = surface.convert_alpha()
    width, height = surface.get_size()
    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    img_data = pygame.image.tostring(surface, "RGBA", True)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glBindTexture(GL_TEXTURE_2D, 0)
    return tex_id, width, height

def init_opengl(window_size):
    global _gl_inited, _window_size
    if _gl_inited:
        return
    _window_size = window_size
    pygame.display.set_mode(window_size, pygame.OPENGL | pygame.DOUBLEBUF)
    glViewport(0, 0, window_size[0], window_size[1])
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 12/255.0, 1.0)
    # set orthographic projection for 2D coordinates (pixel-perfect)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, window_size[0], window_size[1], 0, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    _gl_inited = True

def init_textures():
    global _texture_map, _box_texture, _shader_programs
    # compile shader programs (use shaders from opengl.py)
    try:
        _shader_programs['phong'] = create_shader_program(ogl.phong_vertex, ogl.phong_fragment)
        _shader_programs['gouraud'] = create_shader_program(ogl.gouraud_vertex, ogl.gouraud_fragment)
        _shader_programs['libertiano'] = create_shader_program(ogl.libertiano_vertex, ogl.libertiano_fragment)
    except Exception as e:
        # Se shaders falharem, segue sem eles (programa None)
        print("Shader compile/link error:", e)
        _shader_programs = {'phong': None, 'gouraud': None, 'libertiano': None}

    # carrega texturas dos lixos
    for ttype, path in trash_images.items():
        surf = pygame.image.load(path).convert_alpha()
        surf = pygame.transform.scale(surf, (125, 125))
        tex, w, h = surface_to_texture(surf)
        _texture_map[ttype] = {'tex': tex, 'w': w, 'h': h}

    # box texture
    surfb = pygame.image.load(box_image_path).convert_alpha()
    surfb = pygame.transform.scale(surfb, (125, 125))
    _box_texture, _, _ = surface_to_texture(surfb)

def begin_frame():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

def end_frame():
    pygame.display.flip()

def draw_textured_quad(tex_id, x, y, w, h, program=None):
    if program:
        glUseProgram(program)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glBegin(GL_QUADS)
    
    glTexCoord2f(0, 1); glVertex2f(x, y) 
    
    glTexCoord2f(1, 1); glVertex2f(x + w, y)
    
    glTexCoord2f(1, 0); glVertex2f(x + w, y + h)
    
    glTexCoord2f(0, 0); glVertex2f(x, y + h)
    
    glEnd()
    glBindTexture(GL_TEXTURE_2D, 0)
    if program:
        glUseProgram(0)

def draw_background():
    # simples quad de background (cor já definida em glClearColor)
    pass  # nada adicional necessário (já limpou)

def draw_box(box_obj):
    draw_textured_quad(_box_texture, box_obj.x, box_obj.y, box_obj.size, box_obj.size)

def draw_surface_at(surface, x, y):
    tex, w, h = surface_to_texture(surface)
    draw_textured_quad(tex, x, y, w, h)
    glDeleteTextures([tex])

class Enemie():
    def __init__(self, x, y):
        self.size = 125
        self.type = random.choice(trash_types)
        self.position = pygame.Rect(x, y, self.size, self.size)
        self.spawn_time = time.time()
        self.life_time = 5.0
        self.dead = False
        self.angle = 0.0
        self.scale = 1.0
        # pega textura já carregada
        info = _texture_map.get(self.type)
        self.tex = info['tex'] if info else None
        self.w = info['w'] if info else self.size
        self.h = info['h'] if info else self.size

    def render(self):
        # escolhe shader por tipo
        program = None
        if self.type == "organico":
            program = _shader_programs.get('libertiano')
        elif self.type == "vidro":
            program = _shader_programs.get('gouraud')
        elif self.type in ("plastico", "metal"):
            program = _shader_programs.get('phong')
        # fallback se program None
        draw_textured_quad(self.tex, self.position.x, self.position.y, self.position.width, self.position.height, program)

    def update(self):
        time_alive = time.time() - self.spawn_time
        if time_alive >= self.life_time:
            self.dead = True
            self.angle += 5
            self.scale -= 0.03
            if self.scale <= 0:
                return True
            center = self.position.center
            # continua usando surface transform para o sprite de fallback local (não usado para GL)
            return False
        return False

def generate_enemies():
    margin = 10
    max_x = max(0, defaults.WINDOW_WIDTH - 125 - margin)
    max_y = max(0, defaults.WINDOW_HEIGHT - 125 - margin)
    x = random.randint(margin, max_x)
    y = random.randint(margin, max_y)
    return Enemie(x, y)

def spawn():
    global start
    elapsed = time.time() - start
    if elapsed > interval:
        new = generate_enemies()
        enemies_list.append(new)
        start = time.time()
    for e in enemies_list[:]:
        if e.update():
            enemies_list.remove(e)

def apply_distortion():
    global screen_distortion_effect
    now = pygame.time.get_ticks()
    t = (now - distortion_start) / 300.0
    if t >= 1:
        screen_distortion_effect = False
        return
    # efeito simples: desenha overlay semi-transparente cujo alpha oscila com uma senoide
    alpha = 0.25 + 0.25 * math.sin(t * 20)
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glColor4f(0.1, 0.8, 0.1, alpha)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(_window_size[0], 0)
    glVertex2f(_window_size[0], _window_size[1])
    glVertex2f(0, _window_size[1])
    glEnd()
    glPopAttrib()
