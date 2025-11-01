import os
import random
from time import sleep


def generate_sequence(level):
    sequence_numbers = random.sample(range(1, 101), level)
    print(sequence_numbers)
    sleep(0.7)
    os.system('clear')
    return sequence_numbers

generate_sequence(5)