import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]

for i in range (0, 8):
    GPIO.setup(leds[i], GPIO.OUT)

for i in range (5):
    for i in range (0, 8):
        GPIO.output(leds[i], 1)
        time.sleep(0.2)
        GPIO.output(leds[i], 0)

GPIO.cleanup()
