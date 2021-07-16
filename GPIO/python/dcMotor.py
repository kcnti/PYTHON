import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(40,GPIO.IN)
GPIO.setup(38,GPIO.IN)

def testOnOff():
	while True:
		GPIO.output(8,1)
		time.sleep(1)
		GPIO.output(8,0)
		time.sleep(1)

def button():
	while True:
		state = GPIO.input(40)
		state2 = GPIO.input(38)

		if state == False:
			GPIO.output(8,0)
			print(state)

		elif state2 == False:
			GPIO.output(8,1)
def test():
	while True:
		print(state)
		time.sleep(1)
		if state == True:
			GPIO.output(8,1)
		else:
			GPIO.output(8,0)

#testOnOff()
button()
#test()
