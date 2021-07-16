import RPi.GPIO as GPIO
from time import sleep

setupIn = []
setupOut = [8,10]

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(setupIn,GPIO.IN)
GPIO.setup(setupOut,GPIO.OUT)

def auto():
    while True:
        GPIO.output(8,1)
        GPIO.output(10,0)
        print('spin')
        sleep(1)
        GPIO.output(8,1)
        GPIO.output(10,1)
        print('stop')
        sleep(1)
        GPIO.output(8,0)
        GPIO.output(10,1)
        print('rev spin')
        sleep(1)
        GPIO.output(8,1)
        GPIO.output(10,1)
        print('stop')
        sleep(1)
        
def stop():
    GPIO.output(8,1)
    GPIO.output(10,1)
    
auto()
#stop()
        