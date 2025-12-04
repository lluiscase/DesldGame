import pygame
import defaults

def mouseData(event, active_box, list):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            for num, box in enumerate(list):
                if box.position.collidepoint(event.pos):
                    return num, False

    if event.type == pygame.MOUSEMOTION:
        if active_box is not None and 0 <= active_box < len(list):
            item = list[active_box]
            dx, dy = event.rel
            item.position.move_ip(dx, dy)
            return active_box, False

    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1 and active_box is not None and 0 <= active_box < len(list):
            item = list[active_box]
            for drop_box in defaults.trash_boxes:
                if item.position.colliderect(drop_box.position):
                    list.pop(active_box)
                    return None, True
            return None, False

    return active_box, False
