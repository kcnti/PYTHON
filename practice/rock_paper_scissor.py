import random
rps = ['rock','paper','scissor']
while(True):
	me = str(input('Your turn(rock/paper/scissor): '))
	bot = random.choice(rps)
	print('Your opposite choose:',bot)
	if str(me) == str(bot):
		print('tie!')
	elif me == "rock":
		if bot == "paper":
			print("you lose")
		else:
			print("you win")
	elif me == "paper":
		if bot == "scissor":
			print("you lose")
		else:
			print("you win")
	elif me == "scissor":
		if bot == "rock":
			print("you lose")
		else:
			print("you win")
	else:
		print('Please type the correct word')
	if me == "q":
		break
