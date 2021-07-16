n = int(input())
for i in range(n):
    if i%2 == 0:
        a, b = [int(x) for x in input().split()]
    else:
        b, a = [int(x) for x in input().split()]
    if i == 0:
        min_x = a
        max_x = a
        min_y = b
        max_y = b
    min_x = min(min_x, a)
    max_x = max(max_x, a)
    min_y = min(min_y, b)
    max_y = max(max_y, b)
zz = str(input())
if zz == 'Zig-Zag':
    print(min_x, max_y)
else:
    print(max_x, min_y)
