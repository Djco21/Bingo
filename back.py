import classes
from random import randint

def start_game(list_numbers):
    for i in range (1, 90):
        list_numbers.append(classes.Ball(i, False))
    return list_numbers

def undo_last_action(list_numbers):
    list_numbers.pop(-1)
    return list_numbers

def reset_game(list_numbers):
    list_numbers = []
    return list_numbers

def choose_ball(list_numbers, choosen_balls, number):
    list_numbers.remove()
    choosen_balls.append(number)
    choosen_balls.sort()
    return list_numbers, choosen_balls

def pick_random(choosen_balls):
    picked = False
    while not picked:
        r_number = randint(1,90)
        if r_number not in choosen_balls:
            picked = True
    return r_number


balls_list = []
choosen_balls = []

