integer = list(map(int, input().split()))
alphabet = str(input())
integer.sort()

if alphabet.startswith("A") and alphabet.endswith("B"):
    integer[0], integer[1], integer[2] = integer[0], integer[2], integer[1]
    for i in integer:
        print(i, end=' ')
elif alphabet.startswith("B") and alphabet.endswith("A"):
    integer[0], integer[1], integer[2] = integer[1], integer[2], integer[0]
    for i in integer:
        print(i, end=' ')
elif alphabet.startswith("B") and alphabet.endswith("C"):
    integer[0], integer[1], integer[2] = integer[1], integer[0], integer[2]
    for i in integer:
        print(i, end=' ')
elif alphabet.startswith("C") and alphabet.endswith("A"):
    integer.reverse()
    for i in integer:
        print(i, end=' ')
elif alphabet.startswith("C") and alphabet.endswith("B"):
    integer[0], integer[1], integer[2] = integer[2], integer[0], integer[1]
    for i in integer:
        print(i, end=' ')
else:
    for i in integer:
        print(i, end=' ')
