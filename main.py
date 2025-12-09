import pygame
import defaults
import player
import item_trash
import sys

pygame.init()
defaults.init()  # inicializa screen e trash_boxes

clock = pygame.time.Clock()
running = True
active_box = None
score = 0
font = pygame.font.SysFont(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        active_box, scored = player.mouseData(
            event=event,
            active_box=active_box,
            list=item_trash.enemies_list
        )

        if scored:
            score += 1
            item_trash.start_distortion()

            # ⭐ INVERTE AS LIXEIRAS TODA VEZ QUE PONTUA
            defaults.invert_trash_boxes()

    defaults.screen.fill((250, 250, 250))

    item_trash.spawn()

    for box in defaults.trash_boxes:
        box.draw_box(defaults.screen)

    for e in list(item_trash.enemies_list):
        e.sprite_enemie(defaults.screen)

    score_surf = font.render(f"Score: {score}", True, (0, 0, 0))
    defaults.screen.blit(score_surf, (20, 20))

    # overlay de distorção
    item_trash.apply_distortion_overlay(defaults.screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
