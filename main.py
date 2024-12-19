import pygame
pygame.init()

import source
import back
import classes

clock = pygame.time.Clock()
FPS = 60

source.balls_tuple, source.list_buttons = back.start_game()
while source.running:
    clock.tick(FPS)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    #remover isso e substituir por clique no botão
    if keys[pygame.K_g]:
        source.chosen_balls = back.pick_random(source.balls_tuple, source.chosen_balls)
    back.screen_config()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            source.running = False

pygame.quit()