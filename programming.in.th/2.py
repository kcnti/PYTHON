kep = int(input())
klang = int(input())
plai = int(input())
roum = kep+klang+plai
if roum <= 100 and roum >= 80:
    print("A")
elif roum < 80 and roum >= 75:
    print("B+")
elif roum < 75 and roum >= 70:
    print("B")
elif roum < 70 and roum >= 65:
    print("C+")
elif roum < 65 and roum >= 60:
    print("C")
elif roum < 60 and roum >= 55:
    print("D+")
elif roum < 55 and roum >= 50:
    print("D")
else:
    print("F")
                            