from functools import reduce

lst = [1,2,3,4]
lst2 = [5,6,7,8]
def adding(n):
	return n+n

def even(n):
	return n % 2 == 0

def accumulator(acc, item):
#	print(acc,item)
	return acc + item

added = map(adding,lst)
print("Printing added Number:",list(added))	#map
print("Printing Even Number:",list(filter(even,lst)))	#filter

for x in zip(lst,lst2):	#zip
	print(x)

print(reduce(accumulator, lst, 0))	#reduce

print(list(filter(lambda x: x%2 == 0, lst)))	#lambda expression
print(reduce(lambda acc,item: acc + item, lst, 0))