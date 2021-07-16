a = float(input())
L = 0 
U = a
n = 0
while(U!=0):
    U = U//10
    n+=1
U = n
x = (L+U)/2

while (abs(10**x-a) > (1e-10)*max(10**x, a)):
    if 10**x > a:
        U = x
    else:
        L = x
    x = (L+U)/2
print(round(x, 6))
