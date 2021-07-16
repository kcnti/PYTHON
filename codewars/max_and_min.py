def max_and_min(seq1, seq2): 
    # your code here
    merge = seq1+seq2
    min = merge[0]
    max = merge[0]
    ans = []
    for i in merge:
        if(i < min):
            min = i
        if(i > max):
            max = i
    max_dif = max-min
    ans.append(max_dif)
    merge.sort()
    min_dif = merge[1] - merge[0]
    for i in range(len(merge)):
        if(i+1 == len(merge)):
            break
        if(merge[i] in seq1 and merge[i+1] in seq1):
            continue
        if(merge[i+1] - merge[i] < min):
            print(merge[i+1], merge[i])
            min_dif = merge[i+1] - merge[i]
    ans.append(min_dif)
    return tuple(ans)
