# Author: Hemanth Bathini
# Date: 10/16/2024
# Description: This program reads a poem from an input file and stores the poem information,
# and writes a summary to output file.

import os

def main():

    poem_lines = []
    # Prompt the user for the file name and check if it exists
    while True:
        input_file = input("Enter the name of the file to read the poem from: ").strip()
        if os.path.exists(input_file):
            break
        else:
            print(f"The file '{input_file}' does not exist. Please try again.")
    # Open the file for reading
    with open(input_file, 'r') as file:
        title = file.readline().strip()
        author = file.readline().strip()
        for line in file:
            poem_lines.append(line.strip())

    # Open the output file for writing
    with open('Output.txt', 'w') as output_file:
        output_file.write(f"Poem Title: {title}\n")
        output_file.write(f"Author: {author}\n")
        output_file.write(f"Number of lines in the poem: {len(poem_lines)}\n")
        output_file.write("Preview of the first three lines:\n")
        for i in range(min(3, len(poem_lines))):
            output_file.write(f"{poem_lines[i]}\n")

    print(f"Summary has been written to 'Output.txt'")


if __name__ == "__main__":
    main()
