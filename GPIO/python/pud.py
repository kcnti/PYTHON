import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(10,GPIO.OUT)

while(True):
	state = GPIO.input(8)
#	print(state)
	if state == False:
		print('light on\n')
		GPIO.output(10,GPIO.HIGH)
		time.sleep(0.2)
	else:
		GPIO.output(10,GPIO.LOW)
		print('light off\n')
		time.sleep(0.2)
