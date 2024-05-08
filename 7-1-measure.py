import RPi.GPIO as gpio
import matplotlib.pyplot as plt
import time

def d2b(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

def d2dacleds(value):
    sign = d2b(value)
    gpio.output(dac, sign)
    return sign

def adc():
    lev = 0
    for i in range(7, -1, -1):
        lev += 2 ** i
        val1 = d2b(lev)
        gpio.output(dac, val1)
        time.sleep(0.01)
        cmpval = gpio.input(comp)
        if (cmpval == 1):
            lev -= 2 ** i
    return lev

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
leds = [2, 3, 4, 17, 27, 22, 10, 9]
troy = 13
bits = len(dac)
levs = 2 ** bits 
maxVlt = 3.3

gpio.setmode(gpio.BCM)

gpio.setup(troy, gpio.OUT, initial=gpio.LOW)
gpio.setup(dac, gpio.OUT)
gpio.setup(comp, gpio.IN)

gpio.output(troy, 0)

dat_volt = []
dat_time = []

try:
    # начинаем эксперимент
    beg_time = time.time()
    val = 0
    # начинаем заряжать конденсатор
    gpio.output(troy, 1)
    print("charging...")

    # следим за зарядкой
    while (val < 206):
        val = adc()
        print("voltage: ", val)
        d2dacleds(val)
        dat_volt.append(val)
        dat_time.append(time.time() - beg_time)

    # прекращаем зарядку, переходим к разрядке
    gpio.output(troy, 0)
    print("discharging...")

    # следим за разрядкой
    while (val > 178):
        val = adc()
        print("voltage: ", val)
        d2dacleds(val)
        dat_volt.append(val)
        dat_time.append(time.time() - beg_time)
    
    # записываем в файл
    end_time = time.time()

    with open("./settings.txt", "w") as file:
        file.write(str((end_time - beg_time) / len(dat_volt)))
        file.write("\n")
        file.write(str(maxVlt / 256))

    print(end_time - beg_time, " sec")
    print(len(dat_volt) / (end_time - beg_time))
    print(maxVlt / 256)

finally:
    gpio.output(dac, gpio.LOW)
    gpio.output(troy, gpio.LOW)
    gpio.cleanup()

dat_time_str = [str(i) for i in dat_time]
dat_volt_str = [str(i) for i in dat_volt]

with open("data.txt", "w") as file:
    file.write("\n".join(dat_volt_str))

plt.plot(dat_time, dat_volt)
plt.show()
