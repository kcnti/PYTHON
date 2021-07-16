s1, s2, s3, s4 = [float(x) for x in input().split()]
n=0
_max = s1
_min = s1
if s2 > _max:
    _max = s2
if s3 > _max:
    _max = s3
if s4 > _max:
    _max = s4
if s2 < _min:
    _min = s2
if s3 < _min:
    _min = s3
if s4 < _min:
    _min = s4
print(round((s1+s2+s3+s4-_min-_max)/2, 2))
