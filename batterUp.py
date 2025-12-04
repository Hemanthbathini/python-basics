# Author: Hemanth Bathini
# Date: 09/24/2024
# Description: This program simulates the distance a ball flies in a baseball game
# by randomly generating a number between 0 and 450.
# Based on the distance, it prints different outcomes,
# such as scoring a home run, reaching various bases, or making a strike.

import random

ball_distance = random.randint(0, 450)

if ball_distance > 400:
    print("The ball flew", ball_distance, "feet and the batter scored a home run! That's one point for our team!")
elif ball_distance <= 400 and ball_distance >= 135:
    print("The ball flew", ball_distance, "feet and the batter made it to third base!")
elif ball_distance <= 134 and ball_distance >= 10:
    print("The ball flew", ball_distance, "feet and the batter made it to second base!")
elif ball_distance <= 9 and ball_distance >= 1:
    print("The ball flew", ball_distance, "feet because the batter bunted, and made it to first base!")
else:
    print("The batter has made a strike! Oh no!")
