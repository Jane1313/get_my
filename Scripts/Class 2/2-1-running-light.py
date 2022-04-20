import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 25, 8, 7, 12, 16, 20, 21]
j = 0

GPIO.setup(leds, GPIO.OUT)

while j < 3:
    for i in leds:
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)
    j += 1

GPIO.output(leds, 0)

GPIO.cleanup()