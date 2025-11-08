import pygame
from player import Player
import enemies
import defaults

pygame.init()
clock = pygame.time.Clock()
running =True
dt = 0

jogador = Player()

enemies_list =[enemies.generate_enemies() for _ in range(5)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    defaults.screen.fill((0, 0, 12)) 
    jogador.sprite_player()
    for e in enemies_list:
        e.move()
        e.sprite_enemie()
    keys = pygame.key.get_pressed()
    jogador.mov_player(keys,dt)
    pygame.display.flip()
    dt = clock.tick(60) / 100
pygame.quit()