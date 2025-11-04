from flask import Flask, make_response
from score import get_current_score
from utils import BAD_RETURN_CODE

score_html = """
<html>
<head>
    <title>Scores Game</title>
</head>
<body>
    <h1>The score is:</h1>
    <div id="score">{SCORE}</div>
</body>
</html>
"""

error_html = """
<html>
<head>
    <title>Scores Game</title>
</head>
<body>
    <h1>ERROR:</h1>
    <div id="score" style="color:red">{ERROR}</div>
</body>
</html>
"""

app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    Tries to get the current score and returns the appropriate HTML response.
    """
    try:
        score = get_current_score()

        if score >= 0:
            response_html = score_html
            response_code = 200
            html_params = {"SCORE": score}
        else:
            error_message = f"Invalid score data retrieved: {score}. Score must be non-negative."
            raise ValueError(error_message)

    except Exception as e:
        response_html = error_html
        response_code = BAD_RETURN_CODE
        error_message = f"Failed to retrieve score due to: {str(e)}"
        html_params = {"ERROR": error_message}

    return make_response(response_html.format(**html_params), response_code)

app.run(debug=True, port=5000)
