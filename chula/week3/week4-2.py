d, m, y = [int(e) for e in input().split()]
yon = [2, 4, 6, 9 ,11]
y = y - 543
n = 31
if m == 2: #February
    n = 28
    if y%400 == 0:
        n = 29
    elif y%4 == 0 and y%100 != 0:
        n = 29
else:
    for i in yon:
        if m == i:
            n = 30
d = d + 15
if d > n:
    d = d - n
    m = m + 1
if m > 12:
    m = m - 12
    y = y + 1
y = y + 543

print(f'{d}/{m}/{y}')
