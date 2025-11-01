def welcome():
    while True:
            print('Hello please enter your name: ')
            name = str(input())
            print(f'Hi {name} and welcome to the World of Games: The Epic Journey\n')
            break

def start_play():
    games_options = ['Memory Game', 'Guess Game', 'Currency Roulette']

    print('Please choose a game to play:')
    print('1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n'
          '2. Guess Game - guess a number and see if you chose like the computer.\n'
          '3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n')

    while True:
        try:
            user_input = int(input())
            if user_input > len(games_options) or user_input < 1:
                print('Try Again you must to choose 1-3')
            else:
                break
        except ValueError:
            print('Please enter a valid number')

    print('Please choose a game level between 1-5:')
    while True:
        try:
            level = int(input())
            if level < 1 or level > 5:
                print('Try Again you must to choose 1-5')
            else: break
        except ValueError:
            print('Please enter a valid number')

    print(f'Ok you chose the game "{games_options[user_input - 1]}" with level {level}')
