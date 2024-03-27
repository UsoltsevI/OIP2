import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.OUT)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, 0)

p = GPIO.PWM(20, 1000)
p.start(0)

try:
    while True:
        f = float(input("Enter coef: "))
        if (f < 0 or f > 100):
            print("f must be behind 0 and 100")
        else:
            p.ChangeDutyCycle(f)
            print("valtage: ", f * 3.3 / 100)

finally:
    p.stop()
    GPIO.output(20, 0)
    GPIO.cleanup()
