class PlayerCharacter():
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def say(self):
		print("Hello")
		return

player = PlayerCharacter("Earth",20)

print(player.name,player.age)
