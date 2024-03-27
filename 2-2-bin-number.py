import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def int_to_num(x, number):
    for i in range (0, 8):
        number[i] = x // pow(2, 7 - i)
        x = x % pow(2, 7 - i)

dac = [8, 11, 7, 1, 8, 5, 12, 6]
number = [0] * 8

x = 200
int_to_num(x, number)
print(number)

GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, number)

time.sleep(10)

GPIO.output(dac, 0)

GPIO.cleanup()
