import pygame

width, height = 1920, 1080
display = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
font = pygame.font.SysFont('arial black', 45)
pygame.display.set_caption('Bingo DGSTIC')
red_ball_img = pygame.image.load("assets/red_ball.png")
red_ball_img = pygame.transform.scale(red_ball_img,(90,90))
gray_ball_img = pygame.image.load("assets/gray_ball.png")
gray_ball_img = pygame.transform.scale(gray_ball_img,(90,90))
green_ball_img = pygame.image.load("assets/green_ball.png")
green_ball_img = pygame.transform.scale(green_ball_img,(90,90))
button = pygame.image.load("assets/button.png")
button = pygame.transform.scale(button,(400,100))
balls_area = pygame.Rect(0,0,1080,1080)
background = pygame.Rect(0,0,1920,1080)
balls_tuple = []
list_buttons= []
chosen_balls = []
running = True