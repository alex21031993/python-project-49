from brain_games.games.games_logic import name, prime
import random
import prompt

def br_prime():
    name
    print(prime())
    n = 0
    while n < 3:
        question = random.randint(2,50)
        print('Question: ', question)
        your_answer = str(prompt.string("Your answer: "))
        k = 0
        for i in range(2, question // 2 + 1):
            if (question % i == 0):
                k = k+1
        if (k <= 0) and your_answer == 'yes':
            print("Correct!")
            n += 1
            continue
        if (k > 0) and your_answer == 'no':
            print("Correct!")
            n += 1
            continue
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again,",name,"!")
            break
    if n == 3:
        print(f'Congratulations, {name}!')