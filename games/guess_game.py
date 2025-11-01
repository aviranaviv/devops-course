import random

def generate_number(level):
    print('Generate number')
    return random.randint(1, level)

def get_guess_from_user(level):
    print(f'Please choose a game level between 1-{level}:')

    while True:
        guess = int(input())
        if guess < 1 or guess > 5:
            print(f'Try again you must to choose 1-{level}')
        else:
            return guess

def compare_results(actual_number, user_guess):
    if actual_number == user_guess:
        print('You guessed the correct number')
    else:
        print('You guessed the wrong number')


def play(level):
    number = generate_number(level)
    user_guess = get_guess_from_user(level)
    compare_results(number, user_guess)