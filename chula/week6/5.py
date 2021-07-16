def make_int_list(x):
    if x == '': return []
    return [int(a) for a in x.split(' ')]


def is_odd(e):
    return e%2 != 0


def odd_list(alist):
    return [x for x in alist if x%2!=0]


def sum_square(alist):
    return sum([x*x for x in alist])

print(make_int_list(''))

exec(input().split())
