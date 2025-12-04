import pygame
import defaults
import player
import item_trash

pygame.init()
clock = pygame.time.Clock()
running = True
active_box = None
font = pygame.font.SysFont(None, 50)
score = 0

# Inicializa OpenGL e texturas/shaders
item_trash.init_opengl((defaults.WINDOW_WIDTH, defaults.WINDOW_HEIGHT))
item_trash.init_textures()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        active_box, scored = player.mouseData(event=event, active_box=active_box, list=item_trash.enemies_list)
        if scored:
            score += 1
            item_trash.screen_distortion_effect = True
            item_trash.distortion_start = pygame.time.get_ticks()

    # Atualiza lógica
    item_trash.spawn()

    # Render (tudo via OpenGL)
    item_trash.begin_frame()
    item_trash.draw_background()

    for draw_box in defaults.trash_boxes:
        item_trash.draw_box(draw_box)

    for e in item_trash.enemies_list:
        e.render()

    # efeito simples de "distorção" (overlay/flash)
    if item_trash.screen_distortion_effect:
        item_trash.apply_distortion()

    # desenha score (converte surface -> textura e desenha quad)
    score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
    item_trash.draw_surface_at(score_surf, 20, 20)

    item_trash.end_frame()

    clock.tick(60)

pygame.quit()
