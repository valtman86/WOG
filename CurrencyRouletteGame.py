from currency_converter import CurrencyConverter
from random import randint
import pandas as pd
#if __name__ == "__main__":
 #   my_var = 9
  #  print("here I am")
def get_money_interval(d,val):
    c = CurrencyConverter()
    t=c.convert(val, 'USD', 'ILS')
    t=int(t)
    #print(t) #Currency Converted Value from USD to ILS
    liv=int(t-(5-d))
    riv=int(t+(5-d))
    iv = pd.Interval(left=liv, right=riv)
    #print(iv) #interval
    return iv


def get_guess_from_user(val):
    print("Guess what is the value of %s$ from current currency USD to ILS:"%val)
    #print(user_value)
    user_value=check_is_digit()
    return int(user_value)

def check_is_digit():
    a = True
    while a:
        num=input()
        if num.strip().isdigit():
            num=int(num)
            a = False
        else:
            print("This is not a number. Please enter a number")
    return num

def play(n):
    print("<<<<<Welcome to Currency Roulette GAME>>>>>>")
    value = randint(1, 100)
    #print(value) #generated value
    monint=get_money_interval(n,value)
    print("# money interval:",monint)
    user_val=get_guess_from_user(value)
    #print(user_val)
    if user_val in monint:
        print("You won!")
        return True
    else:
        print("You lose!")
        return False

#get_money_interval()
#n=3
#pl=play(n)
#print(pl)



