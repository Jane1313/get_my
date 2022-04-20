import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while (True):
        a = input()
        if (a == 'q'):
            break
        element = int (a)
        GPIO.output(dac, decimal2binary(element))
        print(3.3/256*element)
except ValueError:
    print ("Wrong input")
except RuntimeError:
    print ("Too big number")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()