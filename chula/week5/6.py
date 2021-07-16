n = int(input())
arr = [str(n)]
while(n!=1):
    if n%2 == 0:
        n = int(n/2)
    else:
        n = (n*3) + 1

    arr.append(str(n))

if len(arr) < 15:
    print('->'.join(arr))
else:
    print('->'.join(arr[len(arr)-15:]))
