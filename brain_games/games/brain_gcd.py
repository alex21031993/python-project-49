#!/usr/bin/env python3
from brain_games.games.games_logic import name, gcd
from random import randint
import math
import prompt

def br_gcd():
    name
    print(gcd())
    n = 0
    while n < 3:
        a = randint(1,10)
        b = randint(1,10)
        print('Question: ', a, b)
        your_answer = str(prompt.string("Your answer: "))
        answer = str(math.gcd(a, b))
        if answer == your_answer:
            print("Correct!")
            n += 1
            continue
        else:
            print(f"{your_answer} is wrong answer ;(. Correct answer was {answer}.")
            print(f"Let's try again, {name}!")
            break
    if n == 3:
        print(f'Congratulations, {name}!')


