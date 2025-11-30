import pygame
import defaults
                             
def mouseData(event,active_box,list):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            for num, box in enumerate(list):
                if box.position.collidepoint(event.pos):
                    return num
                
    if event.type == pygame.MOUSEMOTION:
        if active_box is not None:
            item = list[active_box]
            item.position.move_ip(event.rel)
            item.transf = True
            center = item.position.center
            item.sprite = pygame.transform.scale_by(item.sprite, 1.05)
            item.position = item.sprite.get_rect(center=center)

    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1 and active_box is not None:
            item = list[active_box]
            for drop_box in defaults.trash_boxes:
                if  item.position.colliderect(drop_box.position):
                    list.remove(item)
                    active_box = None
                    
                    break
    return active_box