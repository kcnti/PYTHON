def unique_in_order(iterable):
    lst = []
    for i in iterable:
        if len(lst) < 1 or not i == lst[len(lst) - 1]:
            lst.append(i)

    print(lst)

unique_in_order('AAABBBCCCDDDAABB')