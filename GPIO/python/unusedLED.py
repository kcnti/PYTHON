import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

def a():
	time.sleep(0.01)

while (True):
	GPIO.output(8,1)
	time.sleep(0.01)
	GPIO.output(8,0)
	time.sleep(0.01)
	GPIO.output(10,1)
	time.sleep(0.01)
	GPIO.output(10,0)
	time.sleep(0.01)
	GPIO.output(12,1)
	a()
	GPIO.output(12,0)
	a()
	GPIO.output(16,1)
	a()
	GPIO.output(16,0)
	a()
	GPIO.output(18,1)
	a()
	GPIO.output(18,0)
	a()
	GPIO.output(22,1)
	a()
	GPIO.output(22,0)
	a()
	GPIO.output(24,1)
	a()
	GPIO.output(24,0)
	a()
	GPIO.output(26,1)
	a()
	GPIO.output(26,0)
	a()