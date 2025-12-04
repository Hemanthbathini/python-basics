# Author: Hemanth Bathini
# Date: 09/24/2024
# Description: This program is a guessing game where the user has three chances
# to guess the correct x and y coordinates (between 1 and 10),
# with hints provided after each incorrect guess,
# and the correct coordinates are revealed if all guesses are used.


chances = 3
x_coordinate = 4
y_coordinate = 7

while chances > 0:
    print("The particle is somewhere in this space! You have", chances, "chances to guess it.")
    guess_x = int(input("guess x coordinate between 1 to 10: "))
    guess_y = int(input("guess y coordinate between 1 to 10: "))
    chances -= 1
    if guess_x == x_coordinate and guess_y == y_coordinate:
        print(f"good guess! {x_coordinate, y_coordinate} was the position! ")
        break
    elif guess_x < 1 or guess_x > 10 or guess_y < 1 or guess_y > 10:
        print(f"No good! {(guess_x, guess_y)} is outside of the range!")
    else:
        if guess_x > x_coordinate:
            print("Bad luck! The particle's x position is greater than your x position!")
        elif guess_x < x_coordinate:
            print("Bad luck! The particle's x position is less than your x position!")
        if guess_y > y_coordinate:
            print("Bad luck! The particle's y position is greater than your y position!")
        elif guess_y < y_coordinate:
            print("Bad luck! The particle's x position is less than your x position!")
        if chances == 0:
            print(f"oh no! you ran out of guesses. {(x_coordinate, y_coordinate)} was the particle's position!")
