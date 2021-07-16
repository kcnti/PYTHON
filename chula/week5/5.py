n = [int(x) for x in input().split()]
n.sort()
r = list(set(n))
print(len(r))
if len(r) >= 10:
    print(r[:10])
else:
    print(r)
