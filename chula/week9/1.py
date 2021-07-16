line = int(input())
while line != 0:
    string = input()
    if string.startswith('.'):
        cl = 0
        for i in range(len(string)):
            if string[i+1] != '.':
                cl+=1
                break
            if string[i] == '.':
                cl+=1
        res = int(cl/2)
        string = string[res:]
        print(string)
        line-=1
        continue
    print(string)
    line-=1
