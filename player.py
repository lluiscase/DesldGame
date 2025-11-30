import pygame
import defaults
import main

def mouseData(event,active_box):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            for num, box in enumerate(defaults.enemies_list):
                if box.position.collidepoint(event.pos):
                    return num
    if event.type == pygame.MOUSEMOTION:
        if active_box is not None:
            defaults.enemies_list[active_box].position.move_ip(event.rel)
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1 and active_box is not None:
            item = defaults.enemies_list[active_box]
            for drop_box in defaults.trash_boxes:
                if  item.position.colliderect(drop_box.position):
                    defaults.enemies_list.remove(item)
                    main.score +=1 
                    active_box = None
                    break
    return active_box