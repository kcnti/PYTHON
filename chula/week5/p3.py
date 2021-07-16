m = int(input())
ps1 = 0
ps2 = 0
tried = 0
f = m

def winorlose(p1, p2):
    if p1.lower() == 's' and p2.lower() == 'p':
        return True
    elif p1.lower() == 'p' and p2.lower() == 's':
        return False
    elif p1.lower() == 'p' and p2.lower() == 'r':
        return True
    elif p1.lower() == 'r' and p2.lower() == 'p':
        return False
    elif p1.lower() == 'r' and p2.lower() == 's':
        return True
    elif p1.lower() == 's' and p2.lower() == 'r':
        return False
    else:
        return 'Other'
    return 0

while(True):
    if tried == 3*f:
        break
    if ps1 == f:
        break
    elif ps2 == f:
        break

    p = [x for x in input().split()]
    res = winorlose(p[0], p[1])
    if res == True:
        ps1+=1
        m-=1
    elif res == False:
        ps2+=1
        m-=1
    tried+=1

print(ps1, ps2)
if ps1 > ps2:
    print("Player 1 wins")
elif ps1 == ps2:
    print("Tie")
else:
    print("Player 2 wins")
