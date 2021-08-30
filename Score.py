from pathlib import Path
from os import path
from Utils import SCORES_FILE_NAME

def check_file():
    #my_file = Path("./Score.txt") #original path
    #my_file = Path("./"+str(SCORES_FILE_NAME())) # with
    #my_file = Path('".\\'+str(SCORES_FILE_NAME())+'"')
    my_file = Path(SCORES_FILE_NAME())
    #my_file = path.join("./",SCORES_FILE_NAME())
    #my_file=Path('"'+my_file+'"')
    #print(my_file)
    #my_file = SCORES_FILE_NAME()
    if my_file.is_file():
        #my_file = open("Score.txt", "r")
        my_file = open(SCORES_FILE_NAME(), "r")
        lines = my_file.readlines()
        score=lines[0]
        my_file.close()
        print("Last score:", str(score))
    else:
        #my_file = open("Score.txt", "a")
        my_file = open(SCORES_FILE_NAME(), "a")
        score=0
        my_file.close()
        #print(score)
    return score

def add_score(n):
    DIFFICULTY=int(n)
    POINTS_OF_WINNING = (DIFFICULTY*3)+5
    #print(POINTS_OF_WINNING)
    score=int(check_file())
    score=score+int(POINTS_OF_WINNING)
    print("New score:", str(score))
    my_file = open(SCORES_FILE_NAME(), "w")
    my_file.write(str(score))
    my_file.close()

#user_lv=1
#ads= add_score(user_lv)
#print(ads)
