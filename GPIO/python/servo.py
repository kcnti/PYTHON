import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo = GPIO.PWM(11,50) #pin and hertz
servo.start(2.5) #start with ___
while True:
	servo.ChangeDutyCycle(1)
	sleep(0.5)
	print('0')
	servo.ChangeDutyCycle(7.2)
	sleep(0.5)
	print('90')
	servo.ChangeDutyCycle(14.7)
	sleep(0.5)
	print('180')
servo.stop()
GPIO.cleanup()
