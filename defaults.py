import pygame

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

class BoxTrash():
    def __init__(self, x, y):
        self.size = 125
        self.x = x
        self.y = y
        self.position = pygame.Rect(self.x, self.y, self.size, self.size)
        self.image = pygame.image.load("./img/trash.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
    def draw_box(self):
        screen.blit(self.image, (self.x, self.y))

display_trash = [{"x": 100, "y": 50}, {"x": 1080, "y": 600}, {"x": 100, "y": 600}, {"x": 1080, "y": 50}]
trash_boxes = [BoxTrash(pos["x"], pos["y"]) for pos in display_trash]
