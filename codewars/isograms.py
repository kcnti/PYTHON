def is_isogram(txt):
    lst = []
    for i in txt:
        lst.append(i)
    blst = []
    for _ in lst:
        blst.append(_.upper())
    print(blst)
    for _ in lst:
        if None:
            return True
        elif len(lst) != len(set(blst)):
            return False
        elif (len(lst) == 1):
            return True
        elif len(lst) == len(set(lst)):
            return True

txt = input()
a = is_isogram(txt)
if a:
    print("true")
else:
    print("false")


        

