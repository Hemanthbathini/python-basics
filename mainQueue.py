# Author: Hemanth Bathini
# Date: 11/26/2024
# Description: Reads inputQueue.txt to perform queue operations interactively, handling errors
# gracefully and printing the queue state.

from Queue import Queue, EmptyQueueException


def main():
    queue = Queue()

    try:
        with open("inputQueue.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("enqueue"):
                    _, value = line.split()
                    queue.enqueue(value)
                    print(f"Enqueued: {value}")
                elif line == "dequeue":
                    try:
                        value = queue.dequeue()
                        print(f"Dequeued: {value}")
                    except EmptyQueueException as e:
                        print(e.message)
                elif line == "peek":
                    try:
                        value = queue.peek()
                        print(f"Front of Queue: {value}")
                    except EmptyQueueException as e:
                        print(e.message)
                elif line == "clear":
                    queue.clear()
                    print("Queue cleared.")
                elif line == "print":
                    print(f"Queue: {queue}")
                else:
                    print(f"Unknown operation: {line}")
    except FileNotFoundError:
        print("Input file 'inputQueue.txt' not found.")


if __name__ == "__main__":
    main()
