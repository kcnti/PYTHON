import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 8
ECHO = 7

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while(True):
	GPIO.output(TRIG,False)
	print('Wait for sensor')
	time.sleep(1)
	GPIO.output(TRIG,True)
	time.sleep(0.00001)
	GPIO.output(TRIG,False)


	while(GPIO.input(ECHO) == 0):
		startpulse = time.time()
		#print('record start time',startpulse)
	while(GPIO.input(ECHO) == 1):
		endpulse = time.time()
		#print('record end time')

	duration = endpulse - startpulse
	distance = duration * 17150
	distance = round(distance,2)

	print('Distance:',distance,'cm')
