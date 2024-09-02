#!/usr/bin/env python3
from brain_games.games.games_logic import name, calc
from random import randint, choice
import prompt


def br_calc():
    name
    print(calc())
    n = 0
    while n < 3:
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        choice1 = choice(['+', '-', '*'])
        expression = f'{num1} {choice1} {num2}'
        question = eval(expression)
        print('Question:', expression)
        answer = prompt.string("Your answer: ")
        if str(answer) == str(question):
            print('Correct!')
            n += 1
            continue
        else:
            print(f"{answer} is wrong answer ;(.")
            print(f"Correct answer was {question}.")
            print(f"Let's try again, {name}!")
            break
    if n == 3:
        print(f'Congratulations, {name}!')
