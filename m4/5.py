three = range(1,7)
trip = [[x,y,z] for x in three for y in three for z in three]
for x in trip:
    if sum(x) == 5:
        print (x)
