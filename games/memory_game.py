import os
import random
from time import sleep


def generate_sequence(level):
    sequence_numbers = random.sample(range(1, 101), level)
    print(sequence_numbers)
    sleep(0.7)
    os.system('clear')
    return sequence_numbers

def get_list_from_user(level):
    sequence_numbers = []

    while True:
        try:
            if len(sequence_numbers) < level:
                print(f'Please enter the numbers are you remember')
                sequence_numbers.append(int(input()))
            else:
                break
        except ValueError:
            print('Please enter a valid number')
    return sequence_numbers

def compare_sequence(sequence_numbers, user_sequence_numbers):
    if user_sequence_numbers == sequence_numbers:
        return True
    else:
        return False


def play(level):
    sequence_numbers = generate_sequence(level)
    list_from_user = get_list_from_user(level)
    return compare_sequence(sequence_numbers, list_from_user)