import RPi.GPIO as GPIO
from time import sleep

setupIn = [12,16]
setupOut = [8,10]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(setupIn,GPIO.IN)
GPIO.setup(setupOut,GPIO.OUT)
GPIO.output(8,1)
GPIO.output(10,1)

while True:
    state = GPIO.input(12)
    state2 = GPIO.input(16)
    GPIO.output(8,1)
    GPIO.output(10,1)
    if state == False:
        GPIO.output(8,1)
        GPIO.output(10,0)

    if state2 == False:
        GPIO.output(8,0)
        GPIO.output(10,1)
