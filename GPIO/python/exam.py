import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 7
ECHO = 11
port = [3,5,13] #light
even = [3,13]
odd = [5]

GPIO.setup(port,GPIO.OUT)
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

	if distance >= 5 and distance <= 20:
		GPIO.output(even,1)
		time.sleep(0.5)
		GPIO.output(even,0)
		time.sleep(0.5)
		GPIO.output(odd,1)
		time.sleep(0.5)
		GPIO.output(odd,0)
		time.sleep(0.5)


	elif distance > 20 and distance <= 50:
		GPIO.output(port,1)
		time.sleep(1)
		for x in port:
			GPIO.output(x,0)
			time.sleep(0.1)

	elif distance > 50:
		GPIO.output(port,1)
