
import RPi.GPIO as GPIO
from time import sleep as a


GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.IN)
GPIO.setup(5,GPIO.IN)
GPIO.setup(8,GPIO.IN)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

port = [11,13,15]
for x in port:
	GPIO.setup(x,GPIO.OUT)
while (True):
	state = GPIO.input(3)
	state1 = GPIO.input(5)
	state2 = GPIO.input(8)

	if state == False:
		for y in port:
			GPIO.output(y,1)
			a(0.1)
			GPIO.output(y,0)
			a(0.1)
	if state1 == False:
		for y in port[::-1]:
			GPIO.output(y,1)
			a(0.1)
			GPIO.output(y,0)
			a(0.1)
	if state2 == False:
		for x in range(1,6):
			for y in port:
				GPIO.output(y,1)
			a(0.1)
			for y in port:
				GPIO.output(y,0)
			a(0.1)


