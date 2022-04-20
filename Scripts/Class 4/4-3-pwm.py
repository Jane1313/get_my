import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)

p = GPIO.PWM(24, 1000)
p2 = GPIO.PWM(2, 1000)
p.start(0)
p2.start(0)

try:
    while (True):
        print ("Input the duty cycle:")
        dc = int(input())
        p.ChangeDutyCycle(dc)
        p2.ChangeDutyCycle(dc)
        print ("The voltage is:", 3.3*dc/100)
finally:
    GPIO.output(24, 0)
    GPIO.output(2, 0)
    GPIO.cleanup()
    p.stop()
    p2.stop()
