import RPi.GPIO as gpio
import time

dac = [8, 11, 7, 1, 8, 5, 12, 6]
comp = 14
trk = 13

gpio.setmode(gpio.BCM)

gpio.setup(dac, gpio.OUT)
gpio.setup(trk, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def d2b(val):
    return[int(elem) for elem in bin(val)[2:].zfill(8)]

def adc():
    for i in range(255, 0, -1):
        gpio.output(dac, d2b(i))
        time.sleep(0.01)

        if gpio.input(comp) == gpio.LOW:
            return(i)

    return 0

try:
    while True:
        volt = adc()
        time.sleep(0.01)
        print(volt, "=", volt / 256 * 3.3)

finally:
    gpio.output(dac, 0)
    gpio.output(trk, 0)
    gpio.cleanup()
