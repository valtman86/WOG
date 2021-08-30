from GuessGame import play
from MemoryGame import play as mplay
from CurrencyRouletteGame import play as cplay
from Score import add_score
#from colorama import Fore

def welcome(name):
    name = str("Hello %s and welcome to the World of Games(WoG).\nHere you can find many cool games to play." % name)
    return name

def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    user_in = check_is_digit(3)
    user_lv=user_level(5)
    # Test print what user have chosen
    print("You choose game to play:", user_in)
    print("Game difficulty is:", user_lv)
    #print(user_input(int(user_in)))
    score=user_input(user_in,user_lv)
    if score is True:
        add_score(score)
    return user_in, user_lv

def user_level(l):
    print("Please choose game difficulty from 1 to 5:")
    ul = check_is_digit(l)
    return ul
def check_is_digit(x):
    a = True
    while a:
        num=input()
        if num.strip().isdigit():
            val = int(num)
            #if x ==3 and 1 <= val <=3:
            #    user_input(val)
            #    a = False
            if 1 <= val <=x:
                a = False
            else:
                print("You entered wrong number. Please enter number from 1 to",x)
        else:
            print("This is not a number. Please enter a valid number")
    return num

def user_input(n,l):
#testing with print that function is working
        n=int(n)
        l=int(l)
        if n == 1:
            #print("Memory Game")
            m=mplay(l)
            return m
        elif n == 2:
            #k = "#Guess Game"
            print("#Guess Game")
            #return k
            #os.system("GuessGame.py")
            m=play(l)
            return m
        elif n == 3:
            #print("Currency Roulette")
            m=cplay(l)
            return m