def sum_arrays(array1,array2):
    if not array1 and array2:
        array1, array2 = 0, 0
    lst = []
    lst2 = []
    for i in array1:
        lst.append(str(i))
    for i in array2:
        lst2.append(str(i))
    array1 = ''.join(lst)
    array2 = ''.join(lst2)
    res = int(array1) + int(array2)
    res = [x for x in str(res)]
    if res[0] == '-':
        res[1] = '-'+res[1]
        res.remove('-')
    ans = []
    for i in res:
        ans.append(i)
    ans = list(map(int, ans))
    return ans

sum_arrays([3,2,6,6],[-7,2,2,8])
        