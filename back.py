import classes
import pygame
import source
from random import randint

def start_game():
    list_numbers = []
    for j in range(11):
        for k in range(11):
            if j < 10 and k < 10 and j*10 + k > 0:
                list_numbers.append(classes.Ball(int(j*10 + k), False, 40 + k*100, 40 + j*100))
        balls_tuple = tuple(list_numbers)
    return balls_tuple

def undo_last_action(list_chosen):
    list_chosen.pop(-1)
    return list_chosen

def reset_game(list_chosen):
    list_chosen.clear()
    return list_chosen

def choose_ball(list_numbers, list_chosen, number):
        c_number = number - 1
        list_chosen.append(number)
        list_chosen.sort()
        b_chosen = list_numbers[c_number]
        b_chosen.change_status(True)
        print(b_chosen)
        return list_chosen

def pick_random(list_numbers, list_chosen):
    picked = False
    while not picked:
        r_number = randint(1,99)
        if r_number not in list_chosen:
            picked = True
    else:
        choose_ball(list_numbers, list_chosen, r_number)
        return list_chosen

def screen_config():
    source.display.fill((0,0,0))
    pygame.display.set_caption('Bingo DGSTIC')
    pygame.draw.rect(source.display,(0,0,0), source.background)
    pygame.draw.rect(source.display,(255,255,255), source.balls_area)
    for i in source.balls_tuple:
        i.draw(source.display)
    pygame.display.update()


'''chosen_balls = []

current_input = ''

while current_input != 'end':
    current_input = input('digite o comando: ')
    if current_input == 'iniciar':
        balls_tuple = start_game()
    elif current_input == 'resetar':
        chosen_balls = reset_game(chosen_balls)
    elif current_input == 'escolher':
        chosen_balls = pick_random(balls_tuple, chosen_balls)'''