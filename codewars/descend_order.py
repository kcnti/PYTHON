def descending_order(num):
    # Bust a move right here
    lst = []
    num = str(num)
    for i in num:
        lst.append(i)
    lst = list(map(int, lst))
    lst.sort(reverse=True)
    for i in lst:
        print(str(i), end="")

descending_order(42145)