import matplotlib.pyplot as plt
import numpy as np

data_array = np.loadtxt("data.txt", dtype=float)
data_array = data_array/255*3.3

settings_array = np.loadtxt("settings.txt", dtype=float)

time_array = np.arange(0, len(data_array))
time_array = time_array/settings_array[1]

fig, ax = plt.subplots(figsize=(16,10), dpi=400)
ax.plot(time_array, data_array, linestyle='-', marker='*', color='m', markerfacecolor='#ff22aa')
ax.minorticks_on()
ax.grid(which='major', color = 'blue',    
        linewidth = 1,    
        linestyle = '--') 
ax.grid(which='minor', color = 'blue',    
        linewidth = 0.1,    
        linestyle = '-') 
ax.set_xlabel(u'Время, с')
ax.set_ylabel(u'Напряжение, В')
ax.set_title(u'Процесс заряда и разряда конденсатора в RC-цепочке')
ax.legend ('V(t)')
plt.axis([0, max(time_array)*1.05, 0, max(data_array)*1.05])
fig.savefig("grafic.png")
fig.savefig("grafic.svg")
plt.show()