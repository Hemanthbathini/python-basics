# Author: Hemanth Bathini
# Date: 10-01-2024
# Description: This program allows users to select from different ASCII art options and
# apply a custom symbol border around the art.
# It uses functions to handle user input, display the art with borders,
# and provide a blank canvas if the user's choice is invalid.

def intro():
    print("Welcome to the ASCII Art Painter!")
    print("Here are your options:")
    print("1. Sailing Ship")
    print("2. Sleeping Cat")
    print("3. Turtle")
    print("4. Fish")

    choice = int(input("Enter the number of your choice (1-4): "))
    border = input("Enter a single symbol to use for the border: ")

    return choice, border

def printHeaderFooter(border, size):
    print(border * size)

def sleepingCat(border):
    art = r"""
          |\\   _,, ,---,,_
    ZZZzz /,`.-'`'    -. ;-;;,_
         |,4- ) )-,_. ,\\ ( `'-'
         '---''(_/--' `-'\\_) 
    """
    size = len(art.splitlines()[0]) + 2
    printHeaderFooter(border, size)
    for line in art.splitlines():
        print(f"{border} {line} {border}")
    printHeaderFooter(border, size)

def sailingShip(border):
    art = r"""
    
         | | |
        )_) )_) )_)
       )___))___))___)\\
      )____)____)_____)\\\\
    _____|____|____|____\\\\\\__
     \\ Satisfaction /
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   
    """
    size = len(art.splitlines()[0]) + 2
    printHeaderFooter(border, size)
    for line in art.splitlines():
        print(f"{border} {line} {border}")
    printHeaderFooter(border, size)

def turtle(border):
    art = r"""
        _____     ____
      /      \   /    \
     |        | |      |
      \______/   \____/
    """
    size = len(art.splitlines()[0]) + 2
    printHeaderFooter(border, size)
    for line in art.splitlines():
        print(f"{border} {line} {border}")
    printHeaderFooter(border, size)

def fish(border):
    art = r"""
        ><(((('>
    """
    size = len(art.splitlines()[0]) + 2
    printHeaderFooter(border, size)
    for line in art.splitlines():
        print(f"{border} {line} {border}")
    printHeaderFooter(border, size)

def blank(border):
    size = 10
    printHeaderFooter(border, size)
    for _ in range(5):
        print(f"{border}     {border}")
    printHeaderFooter(border, size)

def main():
    choice, border = intro()

    if choice == 1:
        sailingShip(border)
    elif choice == 2:
        sleepingCat(border)
    elif choice == 3:
        turtle(border)
    elif choice == 4:
        fish(border)
    else:
        blank(border)
        print("The selected painting is not available.")
        exit(-1)

    print("I hope you enjoyed your art!")


if __name__ == "__main__":
    main()
