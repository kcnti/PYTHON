import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 18
port = [3,5,7,11,13,15,19,21,23]
rev_port = []
rev_port.append(port[::-1])
#print(rev_port)
even = [5,11,15,21]
odd = [3,7,13,19,23]

for x in port:
	GPIO.setup(x,GPIO.OUT)

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

	if distance <= 20 and distance >=5:
		for i in range(0,5):
			GPIO.output(port,1)
			time.sleep(0.2)
			GPIO.output(port,0)
			time.sleep(0.2)
	elif distance >= 21 and distance <= 50:
		for m in range(4):
			GPIO.output([port[m],port[7-m]],1)
	#		GPIO.output(port[7-m],1)
			time.sleep(0.5)
			GPIO.output(port[m],0)
			GPIO.output(port[7-m],0)
	#for n in port[::-1]:

	elif distance >= 51 and distance <= 100:
		GPIO.output(even,1)
		time.sleep(0.5)
		GPIO.output(even,0)
		time.sleep(0.5)
		GPIO.output(odd,1)
		time.sleep(0.5)
		GPIO.output(odd,0)
		time.sleep(0.5)


	elif distance >= 101 and distance <= 150:
		GPIO.output(port,1)
		time.sleep(1)
		for x in port:
			GPIO.output(x,0)
			time.sleep(0.1)
	elif distance >= 150:
		GPIO.output(port,0)
