# Author: Hemanth Bathini
# Date: 11/26/2024
# Description: Implements a stack data structure (LIFO) using a linked list, with operations
# like push, pop, peek, clear, and exception handling.

class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class EmptyStackException(Exception):
    def __init__(self, action):
        message = f"Stack is empty; cannot perform '{action}'"
        super().__init__(message)


class Stack:
    def __init__(self):
        self.__head = None

    def push(self, data):
        new_node = Node(data)
        new_node.set_next(self.__head)
        self.__head = new_node

    def pop(self):
        if self.__head is None:
            raise EmptyStackException("pop")
        data = self.__head.get_data()
        self.__head = self.__head.get_next()
        return data

    def peek(self):
        if self.__head is None:
            raise EmptyStackException("peek")
        return self.__head.get_data()

    def clear(self):
        self.__head = None

    def __str__(self):
        current = self.__head
        elements = []
        while current:
            elements.append(str(current.get_data()))
            current = current.get_next()
        return ", ".join(elements)
