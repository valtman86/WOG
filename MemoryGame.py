import numpy as np
import time
import sys

def generate_sequence(n):
        start = 1
        end = 101
        x = np.random.randint(low=start, high=end, size=(n))
        return x


def get_list_from_user(n,ls):
   lst = ls
   print("Enter numbers that you remember:")
   for i in range(0, n):
       print("Please enter element #",i+1,":")
       ele = int(check_is_digit())
       lst.append(ele)
   return ls

def check_is_digit():
    a = True
    while a:
        num=input()
        if num.strip().isdigit():
            val = int(num)
            if 1 <= val <=101:
                a = False
            else:
                print("You entered wrong number. Please enter number from 1 to 101")
        else:
            print("This is not a number. Please enter a valid number from 1 to 101")
    return num

def is_list_equal(l1,l2):
    l1=set(l1)
    l2 = set(l2)
    if l1 == l2:
        print("You won!")
        return True
    else:
        print("You lost!")
        return False
def play(n):
    print("<<<<<Welcome to Memory GAME>>>>>>")
    gs = generate_sequence(n)
    # for i in gs:
    #    print(gs,end=" ")
    #while True:
    wgs=str(gs)
    #print(*wgs)
    sys.stdout.write(wgs)
    time.sleep(2) # better for 2 seconds (0.7)
    sys.stdout.write("\r")
    sys.stdout.flush()
    lst = []
    gl = get_list_from_user(n, lst)
    print("Generate list is :", *gs)
    print("Your list is :", *gl)
    eq = is_list_equal(gs, gl)
    #print(eq)
    return eq