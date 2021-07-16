import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)
GPIO.setup(11,GPIO.OUT)

while(True):
	state = GPIO.input(7)
	print(state)
'''	if state == False:
		print('Button Pressed')
		GPIO.output(11,GPIO.HIGH)
		time.sleep(0.2)
	else:
		GPIO.output(11,GPIO.LOW)'''

