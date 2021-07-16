def factor(N):
    res = []
    for i in range(2, N+1):
        count = 0 
        if N%i == 0:
            while(N%i == 0):
                N = N/i
                count+=1
            res.append([i, count])
    return res

exec(input().strip())
