def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m

def mult_c(c, A):
    res = A.copy()
    for i in range(len(A)):
        for j in range(len(A[0])):
            res[i][j] = A[i][j] * c
    return res

def mult(A, B):
    res = []
    for i in range(len(A)):
        temp = []
        for j in range(len(B[0])):
            temp.append(0)
        res.append(temp)
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j] += A[i][k] * B[k][j]
    return res

A = read_matrix()
B = read_matrix()
print(mult(A, B))

