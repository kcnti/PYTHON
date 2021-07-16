n = input()
lst = []
for i in range(int(n)):
    _input = input().split()
    _type = _input[0]
    if _type == "insert":
        lst.insert(int(_input[1]), _input[2])
    elif _type == "print":
        lst = list(map(int, lst))
        print(lst)
    elif _type == "remove":
        lst.remove(int(_input[1]))
    elif _type == "append":
        lst.append(int(_input[1]))
    elif _type == "sort":
        lst.sort()
    elif _type == "pop":
        lst.pop()
    elif _type == "reverse":
        lst.reverse()
    else:
        print("Err")