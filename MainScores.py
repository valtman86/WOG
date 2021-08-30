
import webbrowser
import os
from Utils import SCORES_FILE_NAME


def read_score():
    my_file = open(SCORES_FILE_NAME(), "r")
    lines = my_file.readlines()
    score =lines[0]
    my_file.close()
    print("Last score:", str(score))
    return score

def score_server():
    issue=score_issue()
    #print(issue)

    if str(issue)=="None":
        score = read_score()

        message = f"""<html>
                <head>
                 <title>Scores Game</title>
                </head>
                <body>
                  <h1>The score is <div id="score">{score}</div></h1>
                </body>
                </html>"""
        return message
    else:
        error = score_issue()
        message = f"""<html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                <body>
                    <h1><div id="score" style="color:red">{error}</div></h1>
                </body>
                </html>"""
        return message

def score_issue():
    try:
        fname=(os.path.basename(SCORES_FILE_NAME()))
        print(fname)
        f = open(SCORES_FILE_NAME(), 'rb')
    except FileNotFoundError:
        issue= f"File {fname} not found."
        return issue
    line = f.readlines()
    #print(line)
    if len(line) == 0:
        issue='The list is empty!'
        return issue


#score_server()
#webbrowser.open_new_tab('MainScores.html')