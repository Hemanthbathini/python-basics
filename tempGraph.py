# Author: Hemanth Bathini
# Date: 10/08/24
# Description: This Python program generates random temperature data for three different
# cities and plots the temperature variations over time using the matplotlib library

import matplotlib.pyplot as plt
import random

time = list(range(1, 13))

city1_temps = []
city2_temps = []
city3_temps = []

for _ in range(12):
    city1_temps.append(random.randint(10, 30))
    city2_temps.append(random.randint(10, 30))
    city3_temps.append(random.randint(10, 30))

plt.plot(time, city1_temps, label='City 1')
plt.plot(time, city2_temps, label='City 2')
plt.plot(time, city3_temps, label='City 3')

plt.title('Temperature Variation Over Time')
plt.xlabel('Time (Months)')
plt.ylabel('Temperature (°C)')

plt.legend(['City 1', 'City 2', 'City 3'])

plt.show()
