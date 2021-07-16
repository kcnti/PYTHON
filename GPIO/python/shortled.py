import RPi.GPIO as GPIO
from time import sleep as a

port = [3,5,13]
GPIO.setmode(GPIO.BOARD)
for x in port:
	GPIO.setup(x,GPIO.OUT)
while (True):
	for y in port:
		GPIO.output(y,1)
		a(0.1)
		GPIO.output(y,0)
		a(0.1)
