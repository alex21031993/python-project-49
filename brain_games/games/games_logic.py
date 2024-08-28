import prompt


def welcome():
    print("Welcome to the Brain Games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name

name = welcome()

def even():
    return print('Answer "yes" if the number is even, otherwise answer "no".')

def calc():
    return print("What is the result of the expression?")

def gcd():
    return print("Find the greatest common divisor of given numbers.")

if __name__ == "__main__":
    welcome

