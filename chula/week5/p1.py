_month = ['January', 'February', 'March' ,'April' ,'May' ,'June', 
        'July' ,'August', 'September', 'October', 'November', 'December']


def dayofyear(d, m, y):
    d = int(d)
    m = int(_month.index(m))+1
    y = int(y)
    # 337 feb not included
    result1 = d
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
    result1+=n

    for i in range(1,13):
        if i >= m:
            break
        if i in yon:
            result1+=30
        if i in kom:
            result1+=31
    return result1

name, month, day, year = [x for x in input().split()]
day = day[:-1]
result1 = dayofyear(day, month, year)

name2, month2, day2, year2 = [x for x in input().split()]
day2 = day2[:-1]

result2 = dayofyear(day2, month2, year2)

if int(year) == int(year2):
    if result1 == result2:
        print(name, name2)
    elif result1 > result2:
        print(name2)
    else:
        print(name)

elif int(year) < int(year2):
    print(name)

else:
    print(name2)
