def sequence(x):
    # Do
    ans = []
    k = 0
    for i in range(1, x+1):
        if i%9 == 0:
            ans.append(i)
            break
        ans.append(i)
    for i in range(10,x+1):
        if (i-9)%10 == 0:
            k = int((i-9)/10)+1
            print(k)
        k+=1
        ans.insert(k, i)
    return ans
