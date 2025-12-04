# Author: Hemanth Bathini
# Date: 10/16/2024
# Description: This program reads integers from a file and computes their average,
# and displays the result

def main():
    # Open the file for reading
    try:
        with open('numbers.txt', 'r') as file:
            total = 0
            count = 0

            # Read each line from the file
            for line in file:
                line = line.strip()
                number = int(line)
                print(number)
                total += number
                count += 1

        # Calculate the average
        if count > 0:
            average = total / count
            print(f"\nThe average of the numbers is: {average}")
        else:
            print("The file is empty. No numbers to calculate an average.")

    except FileNotFoundError:
        print("The file 'numbers.txt' does not exist. Please make sure the file is in the same directory.")
    except ValueError:
        print("The file contains non-numeric data. Please ensure the file only has integer values.")


if __name__ == "__main__":
    main()
