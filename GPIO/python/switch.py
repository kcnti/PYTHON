import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.IN)
GPIO.setup(5,GPIO.IN)
GPIO.setup(8,GPIO.IN)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)



while(True):
	state = GPIO.input(3)
	if state == False:
		print('light on\n')
		GPIO.output(11,GPIO.HIGH)
		time.sleep(0.2)
	else:
		GPIO.output(11,GPIO.LOW)
		print('light off\n')
		time.sleep(0.2)

	state = GPIO.input(5)
	if state == False:
		print('light on\n')
		GPIO.output(13,GPIO.HIGH)
		time.sleep(0.2)
	else:
 		GPIO.output(13,GPIO.LOW)
 		print('light off\n')
 		time.sleep(0.2)

	state = GPIO.input(8)
	if state == False:
		print('light on\n')
		GPIO.output(15,GPIO.HIGH)
		time.sleep(0.2)
	else:
		GPIO.output(15,GPIO.LOW)
		print('light off\n')
		time.sleep(0.2)


