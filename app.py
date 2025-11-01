import sys
# Importing the specific play function is cleaner than importing the whole module
from games.memory_game import play as play_memory
from games.guess_game import play as play_guess
from games.currency_roulette_game import play as play_currency_roulette


def welcome():
    """Prompts the user for their name and prints a welcome message."""
    while True:
        name = input('Hello, please enter your name: ')

        if name.strip():
            print(f'Hi {name.title()} and welcome to the World of Games: The Epic Journey!\n')
            return name.title()
        else:
            print("Name cannot be empty. Please try again.")


def get_game_choice():
    """Prompts the user to choose a game and validates the input."""
    games_map = {
        1: "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.",
        2: "Guess Game - guess a number and see if you chose like the computer.",
        3: "Currency Roulette - try and guess the value of a random amount of USD in ILS."
    }

    print('--- Game Selection Menu ---')
    print('Please choose a game to play:')
    for num, desc in games_map.items():
        print(f'{num}. {desc}')
    print('---------------------------\n')

    while True:
        try:
            choice = int(input(f'Enter your choice (1-{len(games_map)}): '))

            if choice in games_map:
                # Return choice and description for the main loop to store
                return choice, games_map[choice]
            else:
                print(f'❌ Invalid choice. Please choose a number between 1 and {len(games_map)}.')
        except ValueError:
            print('❌ Invalid input. Please enter a valid number.')


def get_level_choice():
    """Prompts the user to choose a game level and validates the input."""
    min_level = 1
    max_level = 5

    print('\n--- Level Selection ---')
    while True:
        try:
            level = int(input(f'Please choose a game level between {min_level}-{max_level}: '))

            if min_level <= level <= max_level:
                return level
            else:
                print(f'❌ Invalid level. Please choose a number between {min_level} and {max_level}.')
        except ValueError:
            print('❌ Invalid input. Please enter a valid number.')

def play(game_choice, game_description, level):
    """Executes the selected game and reports the outcome."""

    game_functions = {
        1: play_memory,
        2: play_guess,
        3: play_currency_roulette
    }

    game_name = game_description.split(' - ')[0]

    print(f'\n🎮 Starting Game: **{game_name}** at Level **{level}**...')

    play_function = game_functions.get(game_choice)

    if play_function:
        try:
            user_win = play_function(level)

            if user_win:
                print('🎉 Congratulations! You win!')
            else:
                print('😔 Sorry, you lost!')
        except Exception as e:
            print(f'An error occurred during game execution: {e}')
    else:
        print('An internal error occurred: Game function not found.')

    print('\n--- Game Over ---')


def user_play_decision(question):
    """Prompts the user for a y/n decision and validates the input."""
    while True:
        user_choice = input(f'{question}\n')
        lower_choice = user_choice.lower()

        if lower_choice == 'y':
            return True
        elif lower_choice == 'n':
            return False
        else:
            print('❌ Please enter y/n')

def play_again():
    """Asks the user if they want to play a game again."""
    return user_play_decision('Do you want to play another game? y/n')


def play_the_same_game():
    """Asks the user if they want to play the same game again."""
    return user_play_decision('Do you want to play the same game again? y/n')


def start_play():
    """Main game loop to handle selection, execution, and replay decisions."""

    get_new_game = True
    game_choice, game_description, level = None, None, None

    while True:
        if get_new_game:
            game_choice, game_description = get_game_choice()
            level = get_level_choice()

        play(game_choice, game_description, level)

        if not play_again():
            print('Goodbye! 👋')
            break

        if play_the_same_game():
            get_new_game = False
        else:
            get_new_game = True