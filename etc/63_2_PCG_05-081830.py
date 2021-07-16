x = [str(x) for x in input().split()]
y = 0
for i in x:
    if i == 'A':
        y+=4
    elif i == 'B':
        y+=3
    elif i == 'C':
        y+=2
    elif i == 'D':
        y+=1
    else:
        y+=0
res = y/len(x)
print(round(res, 2))

