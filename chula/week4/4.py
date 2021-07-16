a = int(input())
L = 0
U = a
x = (L+U)/2
while(abs(10**x-a) > (1e-10)*max(a, 10**x)):
    if 10**x > a:
        U = x
    else:
        L = x
    x = (L+U)/2
print(round(x, 6))
