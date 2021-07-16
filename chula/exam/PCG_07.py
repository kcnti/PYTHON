def histogram_bin( data ):
    # return histogram bin of the given data 
    hist_bin = []
    for e in range(min(data), max(data)+1):
        hist_bin.append(e)
    return hist_bin

def count( data, element ):
    # return the count of the given element in the given data
    c = 0
    for e in data:
        if e == element: c += 1
    return c

#----------------------------------------------------------
def histogram( data ):
    # return 2 lists: (1) histogram bin of the given data
    #                 (2) a list of data frequencies
    hbin = histogram_bin(data)
    lst = []
    for i in hbin:
        lst.append(count(data, i))
    return hbin, lst



#-----------------------------------
exec(input().strip()) # DON'T remove this line
