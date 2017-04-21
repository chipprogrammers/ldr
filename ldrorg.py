import RPi.GPIO as GPIO
from gpiozero import LightSensor, Buzzer
ldr = LightSensor(4)  # alter if using a different pin
while True:
    print(ldr.value)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT)
    if ldr.value>0.5438098907470703:
        GPIO.output(17,False)
    elif ldr.value==0.0:
        GPIO.output(17,True)