# Author: Hemanth Bathini
# Date: 10/16/2024
# Description: This program involves working with files to read input data, process it,
# and generate output

import pbnFunctions

def main():
    """Main function to handle file processing."""
    filename = pbnFunctions.getFileName()
    pbnFunctions.processFile(filename)

    print("Your ASCII art image has been created and saved in 'painting.txt'.")

if __name__ == "__main__":
    main()
