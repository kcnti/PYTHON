def to_gray(img):
    res = []
    for i in img:
        temp = []
        for j in i:
            average = 0
            for k in j:
                average+=k
            temp.append(int(average/3))
        res.append(temp)
    return res

exec(input().strip())
