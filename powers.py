# Author: Hemanth Bathini
# Date: 11/19/2024
# Description: This program calculates the result of a base raised to an exponent using recursion.
# It prints intermediate steps to show the recursive calls at each stage.

def powers(base, exponent):
    print(f"powers({base}, {exponent})")
    if exponent == 1:
        return base

    return base * powers(base, exponent - 1)


def main():
    base = int(input("Enter the base value (integer): "))
    exponent = int(input("Enter the exponent value (integer): "))

    if exponent < 1:
        print("Exponent must be at least 1.")
        return

    result = powers(base, exponent)

    print(f"The result of {base} to the power of {exponent} is: {result}")


if __name__ == "__main__":
    main()
