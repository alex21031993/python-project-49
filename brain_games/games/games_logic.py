import prompt


def welcome():
    print("Welcome to the Brain Games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


name = welcome()


def even():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def calc():
    return "What is the result of the expression?"


def gcd():
    return "Find the greatest common divisor of given numbers."


def progression():
    return "What number is missing in the progression?"


def prime():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


if __name__ == "__main__":
    welcome
