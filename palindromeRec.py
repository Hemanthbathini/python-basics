# Author: Hemanth Bathini
# Date: 11/19/2024
# Description: This program checks if a word is a palindrome using recursion, with a base case for
# single or empty strings.It reduces the string size at each step by removing the first and last characters.

def palinTest(word):
    if len(word) <= 1:
        return True

    if word[0] != word[-1]:
        return False

    return palinTest(word[1:-1])


def main():
    word = input("Enter a word to test if it is a palindrome: ")

    is_palindrome = palinTest(word)

    if is_palindrome:
        print(f'"{word}" is a palindrome.')
    else:
        print(f'"{word}" is not a palindrome.')


if __name__ == "__main__":
    main()
