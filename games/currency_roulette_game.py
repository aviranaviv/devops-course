import random

from currency_converter import CurrencyConverter
converter = CurrencyConverter()

def get_money_interval(level):
    money_generated = random.randint(1, 100)
    print(f'The amount of USD money generated: {money_generated}')
    total_currency = int(converter.convert(money_generated, 'USD', 'ILS'))

    return total_currency - (5 - level), total_currency + (5 - level)


def get_guess_from_user(level):
    print('Add your guess:')

    while True:
        try:
            guess = int(input())
            break
        except ValueError:
            print('Please enter a valid number')

    return guess

def compare_results(actual_number, user_guess):
    print(f'your guess: {user_guess}')
    print(f'actual currency range: {actual_number}')

    if user_guess in range(actual_number[0], actual_number[1]):
        print('You guessed the correct currency!')
        return True
    else:
        print('You guessed the wrong currency!')
        return False

def play(level):
    currency = get_money_interval(level)
    guess = get_guess_from_user(level)

    return compare_results(currency, guess)

