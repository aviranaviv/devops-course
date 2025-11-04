from utils import SCORES_FILE_NAME
def get_current_score():
    """Gets the current score"""
    try:
        score_file = open(SCORES_FILE_NAME, 'r+')
    except FileNotFoundError:
        score_file = open(SCORES_FILE_NAME, 'w+')

    current_score = score_file.readline().strip()
    if current_score == '':
        score_file.write(str(0))
        current_score = 0

    score_file.close()
    return int(current_score)

def update_score(user_score, current_score):
    """Updates the score list"""
    score_file = open(SCORES_FILE_NAME, 'w+')
    new_score = current_score + user_score
    score_file.write(str(new_score))
    score_file.close()

def add_score(difficulty):
    """Adds a score to the score list"""
    user_score = int(difficulty * 3 ) + 5
    current_score = get_current_score()
    update_score(user_score, current_score)