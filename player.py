import pygame
import defaults
#Player properties - speed, life, sprite,hit,collision
initial_pos = pygame.Vector2(defaults.screen.get_width() / 2, defaults.screen.get_height() / 2)


class Player():
    def __init__(self):
        self.life = 10
        self.speed = 30
        self.hit = 0.5
        self.size = 40

    def sprite_player(self):
        square=[
        (initial_pos.x,initial_pos.y),
        (initial_pos.x + self.size,initial_pos.y + self.size),
        (initial_pos.x + self.size, initial_pos.y),
        (initial_pos.x, initial_pos.y +self.size),
        ]
        pygame.draw.polygon(defaults.screen, "red", square, self.size)

    def mov_player(self,keys,dt):
        if keys[pygame.K_w] and initial_pos.y > 0:
            initial_pos.y -= self.speed * dt
        if keys[pygame.K_s] and initial_pos.y < defaults.WINDOW_HEIGTH - self.size:
            initial_pos.y += self.speed * dt
        if keys[pygame.K_a] and initial_pos.x > 0:
            initial_pos.x -= self.speed * dt
        if keys[pygame.K_d] and initial_pos.x < defaults.WINDOW_WIDTH - 66:
            initial_pos.x += self.speed * dt

#def hit():
#def illumination():