import RPi.GPIO as gpio
import time

dac = [8, 11, 7, 1, 8, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
trk = 13

gpio.setmode(gpio.BCM)

gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
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

def volume(val):
    val = int(val / 256 * 10)
    arr = [0] * 8

    for i in range(val - 1):
        arr[i] = 1
    
    return arr

try:
    while True:
        volt = adc()
        time.sleep(0.01)
        gpio.output(leds, volume(volt))
        print(volt, "=", volt / 256 * 3.3)

finally:
    gpio.output(dac, 0)
    gpio.output(trk, 0)
    gpio.cleanup()
