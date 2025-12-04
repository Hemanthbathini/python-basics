# Author: Your Name
# Date: Today's Date
# Description: A program to plot random temperature data for three cities using matplotlib.

import random
import matplotlib.pyplot as plt

# List of months (1 through 12)
time = list(range(1, 13))

# List for three cities
city1_temps = []
city2_temps = []
city3_temps = []

# Generate random temperatures between 10 and 30 for each city
for _ in time:
    city1_temps.append(random.randint(10, 30))
    city2_temps.append(random.randint(10, 30))
    city3_temps.append(random.randint(10, 30))

# Plotting the data
plt.plot(time, city1_temps, label="City 1")
plt.plot(time, city2_temps, label="City 2")
plt.plot(time, city3_temps, label="City 3")

# Adding title and labels
plt.title("Monthly Temperatures for Three Cities")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")

# Adding legend to the graph
plt.legend(["City 1", "City 2", "City 3"])

# Display the graph
plt.show()
