import pygame

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

trash_images = {
    "residuos": "./img/residuos perigosos.png",
    "vidro": "./img/vidro.png",
    "plastico": "./img/plastico.png",
    "papel": "./img/papel.png"
}

class BoxTrash():
    def __init__(self, x, y,trash_type):
        self.size = 125
        self.x = x
        self.y = y
        self.type = trash_type
        self.position = pygame.Rect(self.x, self.y, self.size, self.size)
        self.image = pygame.image.load(trash_images[self.type]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
    def draw_box(self):
        screen.blit(self.image, (self.x, self.y))

display_trash = [{"x": 100, "y": 50,"type":"residuos"}, {"x": 1080, "y": 600,"type":"vidro"}, {"x": 100, "y": 600,"type":"plastico"}, {"x": 1080, "y": 50,"type":"papel"}]
trash_boxes = [BoxTrash(pos["x"], pos["y"],pos["type"]) for pos in display_trash]
