import pygame
from random import randint

pygame.init()
display = pygame.display.set_mode((834, 1080), pygame.FULLSCREEN)
card = pygame.image.load("assets/card.png")
font = pygame.font.SysFont('arial black', 45)
chosen_num = []
class Random_num(object):
    def __init__(self, number, posx, posy):
        self.number = number
        self.x = posx
        self.y = posy

def construct_card(chosen_num):
    for i in range(5):
        for j in range(5):
            if i*j != 9:
                chosen_num.append(Random_num(randint,119+119*j,324+108*i))

def screen():
    display.blit(card,(0,0))
clock = pygame.time.Clock()
FPS = 60
clock.tick(FPS)



