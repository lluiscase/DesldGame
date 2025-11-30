import pygame
import defaults
import player
import item_trash
pygame.init()

clock = pygame.time.Clock()
running =True
dt = 0
active_box =None
score = 0

while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        active_box = player.mouseData(event=event,active_box=active_box,list=item_trash.enemies_list)

    defaults.screen.fill((0, 0, 12)) 

    item_trash.spawn()

    #Desenha os lixos
    for draw_boxes in defaults.trash_boxes:
        draw_boxes.draw_box()
    
    #Desenha os itens que serão jogados fora
    for e in item_trash.enemies_list:
        e.sprite_enemie()
    
    pygame.display.flip()
    dt = clock.tick(60) / 100
pygame.quit()