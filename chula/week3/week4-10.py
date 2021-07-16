n = str(input())
if len(n) <= 3:
    print(n)
if len(n) == 4:
    print(str(round(int(n)/1000, 1)) + "K")
if len(n) == 5 or len(n) == 6:
    print(str(round(int(n)/1000)) + "K")
if len(n) == 7:
    print(str(round(int(n)/1000000, 1)) + "M")
if len(n) == 8 or len(n) == 9:
    print(str(round(int(n)/1000000)) + "M")
if len(n) == 10:
    print(str(round(int(n)/1000000000, 1)) + "B")
if len(n) == 11 or len(n) == 12 or len(n) == 13:
    print(str(round(int(n)/1000000000)) + "B")
