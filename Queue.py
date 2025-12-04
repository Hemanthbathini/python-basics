# Author: Hemanth Bathini
# Date: 11/26/2024
# Description: Implements a queue data structure (FIFO) using a linked list, with operations like enqueue,
# dequeue, peek, clear, and exception handling.

class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node


class EmptyQueueException(Exception):
    def __init__(self, action):
        self.message = f"Queue is empty. Cannot perform '{action}' operation."
        super().__init__(self.message)


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self._tail is None:
            self._head = self._tail = new_node
        else:
            self._tail.set_next(new_node)
            self._tail = new_node

    def dequeue(self):
        if self._head is None:
            raise EmptyQueueException("dequeue")
        data = self._head.get_data()
        self._head = self._head.get_next()
        if self._head is None:
            self._tail = None
        return data

    def peek(self):
        if self._head is None:
            raise EmptyQueueException("peek")
        return self._head.get_data()

    def clear(self):
        self._head = self._tail = None

    def __str__(self):
        current = self._head
        elements = []
        while current is not None:
            elements.append(str(current.get_data()))
            current = current.get_next()
        return ", ".join(elements)
