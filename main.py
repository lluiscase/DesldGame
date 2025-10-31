import pygame
import player
import enemies

pygame.init()
clock = pygame.time.Clock()
running =True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.mov_player(dt)
    player.sprite_player()
    
    pygame.display.flip()
    dt = clock.tick(60) / 100
pygame.quit()