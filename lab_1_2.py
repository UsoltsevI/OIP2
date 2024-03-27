import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.IN )

for i in range(0, 50):
    if GPIO.input(24):
        GPIO.output(25, 1)
    else:
        GPIO.output(25, 0)
    time.sleep(5)
