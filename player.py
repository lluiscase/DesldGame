import pygame
import defaults

size = 40

def sprite_player():
    square=[
    (defaults.initial_pos.x,defaults.initial_pos.y),
    (defaults.initial_pos.x + size,defaults.initial_pos.y + size),
    (defaults.initial_pos.x + size, defaults.initial_pos.y),
    (defaults.initial_pos.x, defaults.initial_pos.y +size),
    ]
    pygame.draw.polygon(defaults.screen, "red", square, size)

def mov_player(dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        defaults.initial_pos.y -= 10 * dt
    if keys[pygame.K_s]:
        defaults.initial_pos.y += 10 * dt
    if keys[pygame.K_a]:
        defaults.initial_pos.x -= 10 * dt
    if keys[pygame.K_d]:
        defaults.initial_pos.x += 10 * dt