string = [str(x) for x in str(input())]
string = set(string)
arr = list()
for i in range(10):
    if str(i) not in string:
        arr.append(str(i))

if len(arr) == 0:
    print("None")
else:
    print(','.join(arr))
