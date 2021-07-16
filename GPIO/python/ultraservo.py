import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 8
ECHO = 7

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(11,GPIO.OUT)
servo = GPIO.PWM(11,50)
servo.start(14.7)

while(True):
	print("Start looping")
	angle = 0
	GPIO.output(TRIG,False)
#	print('Wait for sensor')
	time.sleep(0.1)
	GPIO.output(TRIG,True)
	time.sleep(0.00001)
	GPIO.output(TRIG,False)


	while(GPIO.input(ECHO) == 0):
		startpulse = time.time()
#		print(GPIO.input(ECHO))
#		print('record start time',startpulse)
	while(GPIO.input(ECHO) == 1):
		endpulse = time.time()
#		print(GPIO.input(ECHO))
#		print('record end time')

	duration = endpulse - startpulse
	distance = duration * 17150
	distance = round(distance,2)
	print(distance)
	if distance >= 100:
		continue
	elif distance < 0:
		continue
	servo.ChangeDutyCycle(14.7-(0.15*distance))
	time.sleep(0.5)

#	for x in range(distance):
#	if angle == x:
'''
	if distance == 10:
		angle = 1
	elif distance == 15:
		angle = 2
	elif distance == 20:
		angle = 3
	elif distance == 25:
		angle = 4
	elif distance == 30:
		angle = 5
	elif distance == 35:
		angle = 6
	elif distance == 36:
'''
