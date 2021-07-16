array = []
n=0
while(n!=5):
    a = int(input())
    array.append(a)
    n+=1
array.sort()
print(array[int(len(array)/2)])


