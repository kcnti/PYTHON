n = int(input())
row = n + 1
column = n*2
r = n+1
c = n-1
for i in range(1, row):
    for j in range(1, column):
        if i==n or i+j == r or j-i == c:
            print('*', end='')
        else:
            print(end=' ')
    print()

