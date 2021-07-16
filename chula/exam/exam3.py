x = [float(x) for x in input().split()]
t = 1
c = x.copy()
for i in range(len(c)):
    if i+1 < len(c):
        x.insert(t, (c[i]+c[i+1])/2)
    t+=2
print(x)
