import back
import classes
import pygame

pygame.init()
clock = pygame.time.Clock()
FPS = 60

while True:
    clock.tick(FPS)
    width, height = 1920, 1080
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Bingo DGSTIC')
    display.fill((0,0,0))