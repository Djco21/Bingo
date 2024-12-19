import classes
import pygame
import source
from random import randint

def start_game():
    list_numbers = []
    list_last_calls = []
    call_button = (classes.Button('Chamar Bola',1320,880))
    current_ball = classes.Curr_ball('--',1370,350)
    for i in range(5):
        list_last_calls.append(classes.Last_balls('--', 1280 + i*100,680))
    for j in range(11):
        for k in range(11):
            if j < 10 and k < 10 and j*10 + k > 0:
                list_numbers.append(classes.Ball(int(j*10 + k), False, 40 + k*100, 40 + j*100))
        balls_tuple = tuple(list_numbers)
    return balls_tuple, call_button, current_ball, list_last_calls

def undo_last_action(list_chosen):
    list_chosen.pop(-1)
    return list_chosen

def reset_game(balls_tuple, list_chosen, list_last_call, curr_ball):
    list_chosen.clear()
    curr_ball.change_number('--')
    for i in range(5):
        list_last_call[i].change_number('--')
    for i in balls_tuple:
        i.change_status(False)
    return list_chosen, list_last_call, curr_ball

def choose_ball(list_numbers, list_chosen, list_last_call, curr_ball, number):
        c_number = number - 1
        list_chosen.append(number)
        list_chosen.sort()
        b_chosen = list_numbers[c_number]
        b_chosen.change_status(True)
        present_num = curr_ball.get_number()
        for i in range(4,0,-1):
            curr_object = list_last_call[i]
            next_val = list_last_call[i-1].get_number()
            curr_object.change_number(next_val)
        last_object = list_last_call[0]
        last_object.change_number(present_num)
        curr_ball.change_number(number)
        return list_chosen, list_last_call, curr_ball

def pick_random(list_numbers, list_chosen, list_last_call, curr_ball):
    picked = False
    while not picked:
        r_number = randint(1,99)
        if r_number not in list_chosen:
            picked = True
    else:
        choose_ball(list_numbers, list_chosen, list_last_call, curr_ball, r_number)
        return list_chosen, list_last_call, curr_ball

def screen_config():
    source.display.fill((0,0,0))
    pygame.draw.rect(source.display,(0,0,0), source.background)
    pygame.draw.rect(source.display,(255,255,255), source.balls_area)
    pygame.draw.rect(source.display,(255,255,255), source.last_balls_area)

    
    for i in source.balls_tuple:
        i.draw(source.display)
    source.call_button.draw(source.display)
    for k in range(4,-1,-1):
        source.last_ch_balls[k].draw(source.display)
    source.current_ball.draw(source.display)
    pygame.display.update()