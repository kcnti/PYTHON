def someFunctionReturnGenerator():
	mylist = range(3)
	for i in mylist:
		return i

for i in someFunctionReturnGenerator():
	print(i)