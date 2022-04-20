import matplotlib.pyplot as plt
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









measured_data = [10, 23, 45, 50, 100, 155, 204, 255]
plt.plot (measured_data)
plt.show()

measured_data_str = [str(item) for item in measured_data]
print (measured_data, measured_data_str)

with open("data.txt", "w") as outfile:
	outfile.write ("\n".join (measured_data_str))