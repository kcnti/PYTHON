y = [int(x) for x in input().split()]
ans = 0
for i in range(1, len(y)):
    if i+1 < len(y):
        if y[i] > y[i-1] and y[i] > y[i+1]:
            ans+=1

print(ans)
