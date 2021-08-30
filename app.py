from flask import Flask

from MainScores import score_server
app = Flask(__name__)


@app.route("/")
def index():
    return score_server()
