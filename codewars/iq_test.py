def iq_test(numbers):
    lst = numbers.split()
#    lst = list(map(int, lst))
    even = 0
    odd = 0
    for i in range(len(lst)):
        if (int(lst[i]) % 2 == 0):
            even += 1
        else:
            odd += 1
    pos = 0
    if(odd > even):
        for i in range(0, len(lst)):
            if (int(lst[i]) % 2 == 0):
                pos = i+1
    else:
        for i in range(0, len(lst)):
            if (int(lst[i]) % 2 != 0):
                pos = i+1
    return pos