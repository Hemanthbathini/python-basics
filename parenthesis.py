# Author: Hemanth Bathini
# Date: 11/19/2024
# Description: This program verifies if a series of parentheses is balanced using recursion.

count = 0

def parenTest(paren_line, position):
    global count
    if position == len(paren_line):
        return count == 0

    current_char = paren_line[position]
    if current_char == '(':
        count += 1
    elif current_char == ')':
        count -= 1

    if count < 0:
        return False

    return parenTest(paren_line, position + 1)


def main():
    global count
    count = 0

    paren_line = input("Enter a series of parentheses: ")

    is_balanced = parenTest(paren_line, 0)

    if is_balanced:
        print(f'The series "{paren_line}" is balanced.')
    else:
        print(f'The series "{paren_line}" is not balanced.')


if __name__ == "__main__":
    main()
