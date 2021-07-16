n = 0
while(n!=4):
    _input = str(input())
    if _input == "Sunday":
        print("Red")
    elif _input == "Monday":
        print("Yellow")
    elif _input == "Tuesday":
        print("Pink")
    elif _input == "Wednesday":
        print("Green")
    elif _input == "Thursday":
        print("Orange")
    elif _input == "Friday":
        print("Blue")
    elif _input == "Saturday":
        print("Purple")
    else:
        print("Invalid day")
    n+=1
