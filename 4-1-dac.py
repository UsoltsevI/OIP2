import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def trans(value):
    return [int(element) for element in bin(value)[2:].zfill(8)] 

def is_float(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        print("Enter number: ")
        str = input()

        if (str == "q"):
            print("quit")
            break
        try:
            if (not is_float(str.lstrip('+-'))):
                print("Input not a string")
            elif (not str.lstrip('+-').isnumeric()):
                print("Please, enter int number")
            elif (int(str) < 0 or int(str) > 255):
                print("Please, enter number between 0 and 255")
            else:
                num = int(str)
                trn = trans(num)
                GPIO.output(dac, trn)
                volt = float(num) / 256.0 * 3.3
                print("voltage is about ", volt)
        except Exception:
            if (str == "q"):
                print("quit")
                break

finally:
    GPIO.setup(dac, GPIO.LOW)
    GPIO.cleanup()
