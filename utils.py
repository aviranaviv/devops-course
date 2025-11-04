import os

SCORES_FILE_NAME = 'scores.txt'
BAD_RETURN_CODE = 400

def screen_cleaner():
    """Cleans up the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')