import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
leds = [21,20,16,12,7,8,25,24]

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

GPIO.output(troyka, 1)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    m = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(7):
        m[i] = 1
        GPIO.output(dac, 0)
        GPIO.output(dac, m)
        time.sleep(0.001)
        a = GPIO.input(comp)
        if (a == 0):
            m[i] = 0
    n = 0
    for i in range(7):
        if (m[i] == 1):
            n = n + 2**(7 - i)
        #print (n)
    return n

try:
    while(True):
        x = adc()
        y = x/255*3.3
        print(x," ",y)
        z = int(9*y/3.3)
        print (z)
        b = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(z):
            b[i] = 1
        GPIO.output(leds, b)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()