import random

from currency_converter import CurrencyConverter
converter = CurrencyConverter()

def get_money_interval(level):
    money_generated = random.randint(1, 100)
    total_currency = int(converter.convert(money_generated, 'USD', 'ILS'))
    return total_currency - (5 - level), total_currency + (5 - level)


def get_guess_from_user(level):
    print('Add your guess:')

    while True:
        guess = int(input())
        if guess < 1 or guess > 5:
            print(f'Try again you must to choose 1-{level}')
        else:
            return guess

def compare_results(actual_number, user_guess):
    if actual_number == user_guess:
        print('You guessed the correct currency!')
        return True
    else:
        print('You guessed the wrong currency!')
        return False

def play(level):
    currency = get_money_interval(level)
    guess = get_guess_from_user(level)
    return compare_results(currency, guess)

