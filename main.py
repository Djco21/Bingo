import pygame
pygame.init()

import source
import back
import classes

clock = pygame.time.Clock()
FPS = 60

source.balls_tuple, source.call_button, source.current_ball, source.last_ch_balls = back.start_game()
while source.running:
    clock.tick(FPS)
    
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_ESCAPE]:
    #    pygame.quit()

    back.screen_config()

    if source.call_button.press_button():
        source.chosen_balls, source.last_ch_balls, source.current_ball = back.pick_random(source.balls_tuple, source.chosen_balls, source.last_ch_balls, source.current_ball)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            source.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                source.chosen_balls, source.last_ch_balls, source.current_ball = back.pick_random(source.balls_tuple, source.chosen_balls, source.last_ch_balls, source.current_ball)
            if event.key == pygame.K_r:
                source.chosen_balls, source.last_ch_balls, source.current_ball = back.reset_game(source.balls_tuple, source.chosen_balls, source.last_ch_balls, source.current_ball)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

pygame.quit()