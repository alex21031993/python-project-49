from brain_games.games.games_logic import name, progression
import random
import prompt


def br_progr():
    name
    print(progression())
    n = 0
    while n < 3:
        num = []
        choicenum = []
        num1 = random.randint(0, 10)
        num2 = random.randint(50, 70)
        n1 = random.randint(1, 10)

        for i in range(num1, num2, n1):
            num.append(i)

        choice = random.choice(num)
        x = num.index(choice)
        choice = choicenum.append(choice)
        num[x] = '..'

        print("Question:", num)
        your_answer = str(prompt.string("Your answer: "))

        if your_answer == str(choicenum[0]):
            print("Correct!")
            n += 1
            continue

        else:
            print(f"{your_answer} is wrong answer ;(.")
            print(f"Correct answer was {choicenum[0]}.")
            print(f"Let's try again, {name}!")
            break

    if n == 3:
        print(f'Congratulations, {name}!')
