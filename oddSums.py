# Author: Hemanth Bathini
# Date: 09/24/2024
# Description: This program sums all odd numbers between two randomly generated numbers.

import random

random_integer1 = random.randint(1, 10)
random_integer2 = random.randint(11, 20)
odd_sum = 0
for i in range(random_integer1, random_integer2 + 1):
    if i % 2 != 0:
        odd_sum += i

print(f"the first random number is {random_integer1} ")
print(f"the second random number is {random_integer2} ")
print(f"the sum of odd numbers between two random numbers is: {odd_sum}")
