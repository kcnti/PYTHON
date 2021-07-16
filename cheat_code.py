output = ""
count = 0
line = int(input("Line: "))
while(line != 0):
	code = str(input("Enter cheat code: "))
	for i in code:
		if(count == 17 and i != " "):
			count = 0
			output = output + "+"
			continue
		count+=1
		output+=i
	line-=1
print(output)