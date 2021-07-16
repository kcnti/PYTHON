lst = [5,4,3]

print(list(map(lambda x: x**2, lst)))

lstSort = [(10,-1),(5,3),(1,2),(7,6)]
lstSort2 = lstSort.copy()

lstSort.sort()
lstSort2.sort(key=lambda x: x[1])
print(lstSort,"|",lstSort2)	#sorted with index 0 and index 1