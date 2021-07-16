n = int(input())
arr = list()
j = 1
while(n!=0):
    x, y = [float(x) for x in input().split()]
    fpoint = (x**2+y**2)**1/2
    arr.append([fpoint, j, x, y])
    n-=1
    j+=1

carr = arr.copy()
arr.sort()
a = carr.index(arr[2])+1
print('#{}: ({}, {})'.format(a, arr[2][2], arr[2][3]))
