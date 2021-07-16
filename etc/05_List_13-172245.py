n = int(input())
arr = list()
while(n!=0):
    x = int(input())
    if n%2==0:
        arr.append(x)
    else:
        arr.insert(0, x)
    n-=1

s = [int(x) for x in input().split()]
for i in range(len(s)):
    if len(arr)%2 == 0: # end with front
        if i%2 == 0:
            arr.append(s[i])
        else:
            arr.insert(0, s[i])
    else: # end with back
        if i%2 != 0:
            arr.insert(0, s[i])
        else:
            arr.append(s[i])

a = 0
while(True):
    t = int(input())
    if t == -1:
        break
    if len(arr)%2 == 0: # end with front
        if a%2 == 0:
            arr.append(t)
    else: # end with back
        if a%2 == 0:
            arr.insert(0, t)

print(arr)
