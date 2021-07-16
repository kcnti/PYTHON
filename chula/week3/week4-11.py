d = int(input())
m = int(input())
y = int(input())
# 337 feb not included
result = d
yon = [4, 6, 9 ,11]
kom = [1, 3, 5 ,7 ,8 , 10, 12]
n = 0
y = y - 543
if m >= 2:
    n = 28
    if y%400 == 0:
        n = 29
    elif y%4 == 0 and y%100 != 0:
        n = 29
result+=n

for i in range(1,13):
    if i >= m:
        break
    if i in yon:
        result+=30
    if i in kom:
        result+=31

print(result)

