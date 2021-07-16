n = int(input())
arr = list()

if n%2==0:
    while(n!=0):
        x = int(input())
        if n%2==0:
            arr.append(x)
        else:
            arr.insert(0, x)
        n-=1
else:
    while(n!=0):
        x = int(input())
        if n%2!=0:
            arr.append(x)
        else:
            arr.insert(0, x)
        n-=1

s = input()
s = s.split()


if len(arr)%2 == 0: # end with front
    for i in range(len(s)):
        if i%2 == 0:
            arr.append(int(s[i]))
        else:
            arr.insert(0, int(s[i]))
else:
    for i in range(len(s)): # end with back
        if i%2 != 0:
            arr.append(int(s[i]))
        else:
            arr.insert(0, int(s[i]))
#for i in range(len(s)):
#    if len(arr)%2 == 0: # end with front
#        if i%2 == 0:
#            arr.append(int(s[i]))
#        else:
#            arr.insert(0, int(s[i]))
#    else: # end with back
#        if i%2 != 0:
#            arr.insert(0, int(s[i]))
#        else:
#            arr.append(int(s[i]))

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
