method = input()


if method == "str2RLE":
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


elif method == "RLE2str":
    res = str()
    string = [x for x in input().split()]
    for i in range(0, len(string), 2):
        if i+1 < len(string):
            a = string[i]*int(string[i+1])
            res+=a
            i+=2
    print(res)

else:
    print("Error")
