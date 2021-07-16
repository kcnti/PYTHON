d = [int(x) for x in input().split()]
p = d[-1]
i = -1
j = 0
n = len(d)

while(j < n-1):
    if d[j] <= p:
        i+=1
        d[j], d[i] = d[i], d[j]
    j+=1

d[i+1], d[-1] = d[-1], d[i+1]

print(d)

