import pygame
import defaults

def mouseData(event, active_box, list):
    """
    event: pygame.Event
    active_box: index currently grabbed or None
    list: enemies_list (list of Enemie)
    retorna: (active_box, scored)
    """
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            for num, box in enumerate(list):
                if box.position.collidepoint(event.pos):
                    # seleciona o item e retorna index
                    return num, False

    if event.type == pygame.MOUSEMOTION:
        if active_box is not None:
            item = list[active_box]
            # centraliza o item na posição do mouse
            item.position.center = event.pos
            item.transf = True

    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1 and active_box is not None:
            item = list[active_box]
            for drop_box in defaults.trash_boxes:
                if item.position.colliderect(drop_box.position):
                    # remove o item e pontua
                    item.start_death()
                    return None, True
            # soltou mas não acertou
            return None, False

    return active_box, False
