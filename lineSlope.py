# Author: Hemanth Bathini
# Date: 09/17/24
# Description: This program calculates the slope of a line given two endpoints (x1, y1) and (x2, y2).

# Input coordinates of the two points
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

# Calculate the slope using the formula (y2 - y1) / (x2 - x1)
if x1 == x2:
    print("The slope is undefined (vertical line).")
else:
    slope = (y2 - y1) / (x2 - x1)
    print(f"Starting point: ({x1}, {y1})")
    print(f"Ending point: ({x2}, {y2})")
    print(f"Slope of the line = {slope}")
