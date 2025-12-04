# Author: Hemanth Bathini
# Date: 10/16/2024
# Description: This program involves working with files to read input data, process it,
# and generate output

import os

def getFileName():
    """Prompts the user for a file name and checks if it exists."""
    while True:
        file_name = input("Enter the name of the file to read numbers from: ")
        if os.path.exists(file_name):
            return file_name
        else:
            print(f"The file '{file_name}' does not exist. Please try again.")

def convertLine(line):
    """Converts a line of numbers (comma-separated) into a line of symbols."""
    line = line.strip()
    newLine = ""
    number_list = line.split(',')

    for number in number_list:
        if number == '1':
            newLine += " "
        elif number == '2':
            newLine += ","
        elif number == '3':
            newLine += "_"
        elif number == '4':
            newLine += "("
        elif number == '5':
            newLine += "O"
        elif number == '6':
            newLine += ")"
        elif number == '7':
            newLine += "-"
        elif number == '8':
            newLine += '"'
    return newLine


def processFile(filename):
    """Reads an input file, converts lines into symbols, and writes to an output file."""
    with open(filename, 'r') as input_file:
        with open('painting.txt', 'w') as output_file:
            for line in input_file:
                newLine = convertLine(line)
                output_file.write(newLine + '\n')

    print("Processing complete. The image has been saved to 'painting.txt'.")
