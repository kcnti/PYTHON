string = str(input())
string+=' '
arr = []
k = 0
for i in range(len(string)):
    if i+1 < len(string):
        if string[i] != string[i+1] or string[i+1] == ' ':
            arr.append(string[i])
            k+=1
            arr.append(str(k))
            k = 0
        if string[i] == string[i+1]:
            k+=1

print(' '.join(arr))
