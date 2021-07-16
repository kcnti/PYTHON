string = str(input())
if string.islower():
    print("All Small Letter")
elif string.isupper():
    print("All Capital Letter")
elif not string.islower() and not string.isupper():
    print("Mix")