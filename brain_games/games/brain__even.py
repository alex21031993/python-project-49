from brain_games.games.games_logic import name, even
from random import randint
import prompt


def br_even():
    name
    print(even())
    n = 0
    while n < 3:
        question = randint(1, 100)
        print('Question:', question)
        answer = prompt.string("Your answer: ")
        if question % 2 == 0 and answer == 'yes':
            print('Correct!')
            n += 1
            continue
        if question % 2 != 0 and answer == 'no':
            print("Correct!")
            n += 1
            continue
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
    if n == 3:
        print(f'Congratulations, {name}!')
