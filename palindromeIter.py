# Author: Hemanth Bathini
# Date: 11/19/2024
# Description: This program determines if a user-provided word is a palindrome by comparing characters
# iteratively from both ends.It outputs whether the word is a palindrome.

def palinTest(word):
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True


def main():
    word = input("Enter a word to test if it is a palindrome: ")

    is_palindrome = palinTest(word)

    if is_palindrome:
        print(f'"{word}" is a palindrome.')
    else:
        print(f'"{word}" is not a palindrome.')


if __name__ == "__main__":
    main()
