from random import randint

randnum = randint(1,10)

while True:
	try:
		userin = int(input("Guessing what number:	"))
		if 0 < userin < 11:
			if userin == randnum:
				print("You win!")
				break
			else:
				print("Try Again!")
	except ValueError:
		print("Please re-enter the number")
		continue
