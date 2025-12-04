# Author: Hemanth Bathini
# Date: 10-01-2024
# Description: This program allows users to select from different ASCII art options and
# apply a custom symbol border around the art.
# It uses functions to handle user input, display the art with borders,
# and provide a blank canvas if the user's choice is invalid.

def intro():
    """
    Welcomes the user, provides art options, and takes input for the choice of art and border symbol.

    Returns:
        art_choice (int): User's choice of art.
        border_symbol (str): User's selected symbol for the border.
    """
    print("Welcome to the ASCII Art Painter!")
    print("Choose one of the following artworks:")
    print("1. Sleeping Cat")
    print("2. Sailing Ship")
    print("3. Custom Art 1")
    print("4. Custom Art 2")

    art_choice = int(input("Enter the number of your choice: "))
    border_symbol = input("Enter the symbol you would like for the border: ")

    return art_choice, border_symbol


def printHeaderFooter(border, size):
    """
    Prints a border line of the specified symbol and size.

    Parameters:
        border (str): The symbol to use for the border.
        size (int): The number of times to repeat the border symbol.
    """
    print(border * size)


def sleepingCat(border):
    """
    Displays the 'sleeping cat' ASCII art with borders.

    Parameters:
        border (str): The symbol to use for the border.
    """
    art = [
        "   /\\_/\\  ",
        "  ( o.o ) ",
        "   > ^ <  "
    ]

    printHeaderFooter(border, 15)
    for line in art:
        print(f"{border} {line} {border}")
    printHeaderFooter(border, 15)


def sailingShip(border):
    """
    Displays the 'sailing ship' ASCII art with borders.

    Parameters:
        border (str): The symbol to use for the border.
    """
    art = [
        "     __/\\__",
        "   /      \\",
        "   \\______/"
    ]

    printHeaderFooter(border, 15)
    for line in art:
        print(f"{border} {line} {border}")
    printHeaderFooter(border, 15)


def customArt1(border):
    """
    Displays a custom ASCII art #1 with borders.

    Parameters:
        border (str): The symbol to use for the border.
    """
    art = [
        "    [====]",
        "    \\ || /",
        "     \\__/ "
    ]

    printHeaderFooter(border, 15)
    for line in art:
        print(f"{border} {line} {border}")
    printHeaderFooter(border, 15)


def customArt2(border):
    """
    Displays a custom ASCII art #2 with borders.

    Parameters:
        border (str): The symbol to use for the border.
    """
    art = [
        "   _______ ",
        "  |       |",
        "  |_______|"
    ]

    printHeaderFooter(border, 15)
    for line in art:
        print(f"{border} {line} {border}")
    printHeaderFooter(border, 15)


def blank(border):
    """
    Displays a blank canvas with borders.

    Parameters:
        border (str): The symbol to use for the border.
    """
    printHeaderFooter(border, 15)
    for _ in range(5):
        print(f"{border}       {border}")
    printHeaderFooter(border, 15)
