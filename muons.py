# Author: Hemanth Bathini
# Date: 10/08/24
# Description: This Python program simulates a Muon Capture Rate Map for a 8x8 grid.
# It generates random capture rates and identifies the highest and lowest rates,
# along with their respective coordinates.

import random

MAP_SIZE = 8

muon_map = [[0 for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

for i in range(MAP_SIZE):
    for j in range(MAP_SIZE):
        muon_map[i][j] = random.randint(0, 500)

highest_capture_rate = -1
lowest_capture_rate = 501
highest_x = highest_y = -1
lowest_x = lowest_y = -1

for i in range(MAP_SIZE):
    for j in range(MAP_SIZE):
        if muon_map[i][j] > highest_capture_rate:
            highest_capture_rate = muon_map[i][j]
            highest_x, highest_y = i, j
        if muon_map[i][j] < lowest_capture_rate:
            lowest_capture_rate = muon_map[i][j]
            lowest_x, lowest_y = i, j

print(f"Highest capture rate: {highest_capture_rate} at coordinates ({highest_x + 1}, {highest_y + 1})")

print(f"Lowest capture rate: {lowest_capture_rate} at coordinates ({lowest_x + 1}, {lowest_y + 1})")

print("\nMuon capture rate map (8x8 grid):")
for row in muon_map:
    for val in row:
        print(f"{val:4}", end=" ")
    print()

