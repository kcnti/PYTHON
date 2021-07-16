N = int(input())
list_name = {}

for i in range(1, N+1):
    name = input().split()
    list_name[name[0]] = name[1]

M = int(input())
for i in range(M):
    name = input()
    res = name
    for k,v in list_name.items():
        if k == name:
            res = v
        elif v == name:
            res = k
    print('Not found' if res == name else res)
