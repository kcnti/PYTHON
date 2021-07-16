n = int(input())
zz = []
while(n!=0):
    s1, s2 = [zz.append(int(x)) for x in input().split()]
    n-=1

method = str(input())
zig = 0
zag = 1
if method == 'Zig-Zag': # min start with 1
    _min = zz[1]
    _max = zz[2]
    for i in range(zig, len(zz), 2):
        if _min > zz[i]:
            _min = zz[i]
    for i in range(zag, len(zz), 2):
        if _max < zz[i]:
            _max = zz[i]
    print(_min, _max)

if method == 'Zag-Zig': # min start with 2
    _min = zz[2]
    _max = zz[1]
    for i in range(zag, len(zz), 2):
        if _min > zz[i]:
            _min = zz[i]
    for i in range(zig, len(zz), 2):
        if _max < zz[i]:
            _max = zz[i]
    print(_max, _min)
