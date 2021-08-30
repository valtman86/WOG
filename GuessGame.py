import random
#from Live import check_is_digit
def generate_number(x):
    num = random.randint(1, x)
    return  num

def get_guess_from_user(x):
    #x=str(x)
    print("Please enter number between 1 to %s"%x)
    num= check_is_digit(x)
    return num

def compare_results(a,b):
    a=int(a)
    b=int(b)
    if a > b:
        print("You lose")
        return False
    elif a <= b:
        print("You won")
        return True
    else:
        return "Try againe"

def play(l):
#lg = load_game()
#user_level =int(lg[1])
#user_level =int(user_level[0])
    print("<<<<<Welcome to Guess GAME>>>>>>")
    user_level=int(l)
    secret_number =generate_number(user_level)
    print("#Secret number:",secret_number)
    gg=get_guess_from_user(user_level)
    print("#Get guess from user: ", gg)
    res=compare_results(secret_number,gg)
    #print(res)
    return res

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