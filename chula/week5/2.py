# Name : Nickname
name = {"Robert":"Dick", "William":"Bill", "James":"Jim", "John":"Jack",
        "Margaret":"Peggy", "Edward":"Ed", "Sarah":"Sally", "Andrew":"Andy",
        "Anthony":"Tony", "Deborah":"Debbie"}

n = int(input())
while(n!=0):
    x = str(input())
    t = 0
    for element in name:
        if x == element:
            print(name[element])
            t+=1
            break
        elif x == name[element]:
            t+=1
            print(element)
            break
    if t == 0:    
        print("Not found")
    n-=1

