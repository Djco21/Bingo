import pygame
pygame.init()

import source
import back
import classes

clock = pygame.time.Clock()
FPS = 60

while source.running:
    clock.tick(FPS)
    
    '''keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()'''
    source.balls_tuple = back.start_game()
    back.screen_config()

pygame.quit()