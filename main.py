import pygame
from player import Player
from enemies import Enemie
import defaults

pygame.init()
clock = pygame.time.Clock()
running =True
dt = 0

jogador = Player()
inimigo = Enemie()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    defaults.screen.fill((0, 0, 12)) 
    inimigo.sprite_enemie()
    inimigo.move()
    jogador.sprite_player()
    keys = pygame.key.get_pressed()
    jogador.mov_player(keys,dt)
    pygame.display.flip()
    dt = clock.tick(60) / 100
pygame.quit()