def digital_root(n):
    #a = [int(i) for i in str(n)]
    b = list(map(int,str(n)))
    if len(b) != 1:
        return digital_root(sum(b))
    else:
        return sum(b)

digital_root(964)