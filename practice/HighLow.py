import random
while(True):
    hilow = str(input("High or Low: "))
    if hilow != "High" and hilow != "Low":
        print("TYPE HIGH OR LOW")
        break
    a = random.randint(1,10)
    print("Random number is",a)
    if a >= 6:
        if hilow == "High":
            print("YOU WIN!!")
        else:
            print("WHAT A LOSER!")
    elif a <= 5:
        if hilow == "Low":
            print("YOU WIN!!")
        else:
            print("WHAT A LOSER!")
        