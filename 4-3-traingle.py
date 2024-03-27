import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

direct = 1
x = 0

try:
    period = float(input("Eneter a period, please: "))

    while True:
        GPIO.output(dac, dec2bin(x))
        volt =  x / 256 * 3.3
        print("voltage: ", volt)

        if x == 0: 
            direct = 1
        if x == 255: 
            direct = 0

        if direct == 1:
            x += 1
        else:
            x -= 1
        
        sleep(period/512)

except ValueError:
    print("Enter valid period!")

finally:
    GPIO.setup(dac, GPIO.LOW)
    GPIO.cleanup()
