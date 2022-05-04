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

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        GPIO.output(dac, decimal2binary(i))
      
        time.sleep(0.001)
        a = GPIO.input(comp)
        if (a == 0):
            break
    GPIO.output(dac, 0)
    GPIO.output(leds, decimal2binary(i))
    #y = i/255*3.3
    return i            #возвращает значение напряжения на выходе тройки

try:
	measured_data = []
	t_0 = time.time()

	GPIO.output(troyka, 1)
	u = adc()
	while (u <= 0.97*255):
		u = adc()
		measured_data.append(u)
		time.sleep(0.001)

	GPIO.output(troyka, 0)
	while (u >= 0.02*255):
		u = adc()
		measured_data.append(u)
		time.sleep(0.001)

	t_1 = time.time()
	delta_t = t_1 - t_0

	step_quant = 3.3/256
	sr_v_diskr = len(measured_data) / delta_t
	period = delta_t / len(measured_data)

	plt.plot (measured_data)
	plt.show()

	measured_data_str = [str(item) for item in measured_data]
	step_quant_str = str(step_quant)
	sr_v_diskr_str = str(sr_v_diskr)

	with open("data.txt", "w") as outfile:
		outfile.write ("\n".join (measured_data_str))

	with open("settings.txt", "w") as outfile:
		outfile.write (step_quant_str)
		outfile.write ("\n")
		outfile.write (sr_v_diskr_str)

	print("Продолжительность эксперимента: ", delta_t, ",период: ", period, ", частота:", sr_v_diskr)

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()