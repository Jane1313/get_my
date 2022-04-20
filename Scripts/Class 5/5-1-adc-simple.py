import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        GPIO.output(dac, decimal2binary(i))
        time.sleep(0.01)
        a = GPIO.input(comp)
        if (a == 0):
            break
    GPIO.output(dac, 0)
    print (i)
    return i

try:
    while(True):
        x = adc()
        y = x/255*3.3
        print(x," ",y)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()