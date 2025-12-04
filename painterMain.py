# Author: Hemanth Bathini
# Date: 10-01-2024
# Description: This program allows users to select from different ASCII art options and
# apply a custom symbol border around the art.
# It uses functions to handle user input, display the art with borders,
# and provide a blank canvas if the user's choice is invalid.

import painterFuncs

def main():
    """
    The main function to coordinate the ASCII painting program.
    """
    art_choice, border_symbol = painterFuncs.intro()

    if art_choice == 1:
        painterFuncs.sleepingCat(border_symbol)
    elif art_choice == 2:
        painterFuncs.sailingShip(border_symbol)
    elif art_choice == 3:
        painterFuncs.customArt1(border_symbol)
    elif art_choice == 4:
        painterFuncs.customArt2(border_symbol)
    else:
        painterFuncs.blank(border_symbol)
        print("Sorry, we don't have that painting.")

    print("We hope you enjoyed your art!")


if __name__ == "__main__":
    main()
