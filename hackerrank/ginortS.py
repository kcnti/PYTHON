n = input()
l = []
lower = []
up = []
even = []
odd = []
num = []
for i in n:
    l.append(i)
for i in l:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        up.append(i)
    elif i.isnumeric():
        num.append(i)
num = list(map(int, num))
for i in num:
    if (i % 2 == 1):
        even.append(i)
    elif (i%2 == 0):
        odd.append(i)
even.sort()
odd.sort()
even.extend(odd)
lower.sort()
for i in lower:
    print(i, end='')
up.sort()
for i in up:
    print(i, end='')
for i in even:
    print(i, end='')