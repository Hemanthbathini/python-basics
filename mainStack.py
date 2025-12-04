# Author: Hemanth Bathini
# Date: 11/26/2024
# Description: Reads inputStack.txt to perform stack operations interactively, such as push, pop, peek, and clear,
# handling exceptions gracefully and displaying the stack's state.

from Stack import Stack, EmptyStackException


def main():
    stack = Stack()

    with open("inputStack.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("push"):
                value = line.split(" ")[1]
                stack.push(value)
                print(f"Pushed {value} onto the stack.")
            elif line == "pop":
                try:
                    popped_value = stack.pop()
                    print(f"Popped {popped_value} off the stack.")
                except EmptyStackException as e:
                    print(e)
            elif line == "peek":
                try:
                    top_value = stack.peek()
                    print(f"Top of stack: {top_value}")
                except EmptyStackException as e:
                    print(e)
            elif line == "clear":
                stack.clear()
                print("Stack cleared.")
            else:
                print(f"Stack contents: {stack}")


if __name__ == "__main__":
    main()
