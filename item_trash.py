import pygame
import defaults
import random
import time
import math

enemies_list = []
_start_time = time.time()
interval = 2.0

distortion_active = False
distortion_start = 0
distortion_duration_ms = 300.0

_window_size = (defaults.WINDOW_WIDTH, defaults.WINDOW_HEIGHT)

ENEMY_TYPES = [
    "./img/lixo_papel.png",
    "./img/lixo_residuo.png",
    "./img/lixo_vidro.png",
    "./img/lixo_plast.png"
]


class Enemie:
    def __init__(self, x, y):
        self.size = 125
        self.transf = False
        
        # posição
        self.position = pygame.Rect(x, y, self.size, self.size)

        # escolher sprite aleatório
        img_path = random.choice(ENEMY_TYPES)
        self.sprite = pygame.image.load(img_path).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (self.size, self.size))

        # animação de "morte"
        self.is_dying = False
        self.death_start = 0
        self.death_duration = 350  # ms

    def start_death(self):
        """Inicia o fade + distorção ao remover"""
        self.is_dying = True
        self.death_start = pygame.time.get_ticks()

    def sprite_enemie(self, surface):
        """Render normal ou animação de remoção"""
        if not self.is_dying:
            surface.blit(self.sprite, self.position)
            return

        # tempo da animação
        now = pygame.time.get_ticks()
        t = (now - self.death_start) / self.death_duration

        if t >= 1:
            # terminou → remover "de fato"
            if self in enemies_list:
                enemies_list.remove(self)
            return

        # ----- Distorção: escala, offset, alpha -----

        scale = 1 + 0.25 * math.sin(t * 30)   # tremida
        fade = max(0, 255 - int(t * 255))     # fade-out
        offset_x = int(5 * math.sin(t * 40))  # deslocamento horizontal
        offset_y = int(5 * math.cos(t * 40))  # deslocamento vertical

        # redimensionar sprite
        new_size = int(self.size * scale)
        temp = pygame.transform.smoothscale(self.sprite, (new_size, new_size))
        temp.set_alpha(fade)

        # reposicionar no centro
        rect = temp.get_rect(center=self.position.center)

        # aplicar tremida
        rect.x += offset_x
        rect.y += offset_y

        surface.blit(temp, rect)


def generate_enemies():
    w = defaults.screen.get_width()
    h = defaults.screen.get_height()
    margin = 10
    x = random.randint(margin, w - 135)
    y = random.randint(margin, h - 135)
    return Enemie(x, y)


def spawn():
    global _start_time
    if time.time() - _start_time > interval:
        enemies_list.append(generate_enemies())
        _start_time = time.time()


def start_distortion():
    global distortion_active, distortion_start
    distortion_active = True
    distortion_start = pygame.time.get_ticks()


def apply_distortion_overlay(surface):

    global distortion_active
    if not distortion_active:
        return

    now = pygame.time.get_ticks()
    t = (now - distortion_start) / distortion_duration_ms
    if t >= 1:
        distortion_active = False
        return

    alpha = int(80 + 80 * math.sin(t * 20))
    alpha = max(0, min(200, alpha))

    overlay = pygame.Surface(_window_size, pygame.SRCALPHA)
    overlay.fill((30, 255, 80, alpha))

    surface.blit(overlay, (0, 0))
