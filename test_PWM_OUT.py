import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(1,GPIO.OUT)

myPWM=GPIO.PWM(1,255)
myPWM.start(1)

def fonction1():
    compteur=1
    for k in range(100):
        myPWM.ChangeDutyCycle(compteur)
        compteur+=5
        if compteur>=50:
            compteur=1
        sleep(0.1)


fonction1()
myPWM.stop()
GPIO.cleanup()