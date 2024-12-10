import classes
from random import randint

def start_game(list_numbers):
    for i in range (1, 90):
        list_numbers.append(classes.Ball(i, False))
    return list_numbers

def undo_last_action(list_numbers, list_chosen):
    element = list_numbers.pop(-1)
    list_chosen.append(element)
    return list_numbers, list_chosen

def reset_game(list_numbers):
    list_numbers = []
    return list_numbers

def choose_ball(list_numbers, list_chosen, number):
    for i in list_numbers:
        if i.number == number:
            list_numbers.remove(i)
            list_chosen.append(i)
            list_chosen.sort()
            i.change_status(True)
            return list_numbers, list_chosen
    else: 
        return

def pick_random(list_numbers, list_chosen):
    picked = False
    while not picked:
        r_number = randint(1,90)
        for i in list_chosen:
            if r_number == i.number:
                r_number = pick_random(list_chosen)
                break
        else:
            picked = True
    else:
        choose_ball(list_numbers, list_chosen, r_number)

balls_list = []
chosen_balls = []