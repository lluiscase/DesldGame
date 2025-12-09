import pygame
import random

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280

screen = None

trash_images = {
    "residuos": "./img/residuos perigosos.png",
    "vidro": "./img/vidro.png",
    "plastico": "./img/plastico.png",
    "papel": "./img/papel.png"
}

class BoxTrash:
    def __init__(self, x, y, trash_type):
        self.size = 125
        self.x = x
        self.y = y
        self.type = trash_type
        self.position = pygame.Rect(self.x, self.y, self.size, self.size)
        img = pygame.image.load(trash_images[self.type]).convert_alpha()
        self.image = pygame.transform.scale(img, (self.size, self.size))

    def draw_box(self, surface):
        surface.blit(self.image, (self.x, self.y))


# posições base — sempre reaplicadas após inverter
_display_trash = [
    {"x": 100, "y": 50, "type": "residuos"},
    {"x": 1080, "y": 600, "type": "plastico"},
    {"x": 100, "y": 600, "type": "vidro"},
    {"x": 1080, "y": 50, "type": "papel"},
]

trash_boxes = []


def init(window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT):
    global screen, trash_boxes
    screen = pygame.display.set_mode((window_width, window_height))
    trash_boxes = [BoxTrash(pos["x"], pos["y"], pos["type"]) for pos in _display_trash]


# ⭐ NOVA FUNÇÃO — INVERTER A POSIÇÃO DAS LIXEIRAS
def invert_trash_boxes():
    """
    Inverte a ordem das lixeiras e reaplica as posições na nova ordem.
    Exemplo: A B C D → D C B A
    """
    global trash_boxes

    # 1. Inverte a ordem dos objetos
    trash_boxes.reverse()

    # 2. Reaplica as posições originais na nova ordem
    for box, pos in zip(trash_boxes, _display_trash):
        box.x = pos["x"]
        box.y = pos["y"]
        box.position.topleft = (box.x, box.y)
