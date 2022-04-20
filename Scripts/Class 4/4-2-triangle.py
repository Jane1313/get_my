import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    print ("Input the period:")
    period = input()
    p = float(period)/2.0/256.0
    while (True):
        for i in range(255):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(p)
            GPIO.output(dac, 0)
        for i in range(255,0,-1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(p)
            GPIO.output(dac, 0)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()