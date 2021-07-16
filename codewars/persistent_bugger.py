from math import floor
def persistence(n):
    sum =0
    if(len(str(n)) == 1):
        return 0;
    while(True):
        temp = n%10
        temp2 = floor(n/10)
        if(temp*temp2 == 0):
            break
        sum = sum+1
    return sum

print(persistence(39))
