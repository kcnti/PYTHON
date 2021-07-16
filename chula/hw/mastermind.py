# Prog-04: Mastermind Game 
# 6330573721 Name Apichaya Mongkolphinyopas

import random
import math

WINNING_MSG = "Congratulations! You won the game."
LOSING_MSG = "Sorry! You just lost it."

code = ''.join(random.sample('ABCDEF', 4))

print('Please guess the puzzle code using')
print('the four distinct code characters from [A to F]:')

#---------------------------------------------------

#print(code)
# P = both correct
# V = position incorrect but color correct
# X = both incorrect
time = 0

def mastermind(code, guess):
    import sys
    global time
    p = 0
    v = 0
    x = 0
    time+=1
    #-------------------------- P case ---------
    if guess[0] in code and guess[0] == code[0]:
        p+=1
    elif guess[0] in code and guess[0] != code[0]:
        v+=1
    #-----------------
    if guess[1] in code and guess[1] == code[1]:
        p+=1
    elif guess[1] in code and guess[1] != code[1]:
        v+=1
    #-----------------
    if guess[2] in code and guess[2] == code[2]:
        p+=1 
    elif guess[2] in code and guess[2] != code[2]:
        v+=1
    #-----------------
    if guess[3] in code and guess[3] == code[3]:
        p+=1
    elif guess[3] in code and guess[3] != code[3]:
        v+=1
    #-------------------------- X case --------- 
    if guess[0] not in code:
        x+=1
    if guess[1] not in code:
        x+=1
    if guess[2] not in code:
        x+=1
    if guess[3] not in code:
        x+=1
    if p == 4:
        print(WINNING_MSG)
        sys.exit()
    else:
        print("\t  P={},V={},X={}".format(p,v,x))
    if time == 4 and p!= 4:
        print(LOSING_MSG)
        print("The answer is", code)
        print("Please try again...")


turn1 = str(input("Turn #1 : "))
mastermind(code, turn1)
turn2 = str(input("Turn #2 : "))
mastermind(code, turn2)
turn3 = str(input("Turn #3 : "))
mastermind(code, turn3)
turn4 = str(input("Turn #4 : "))
mastermind(code, turn4)



