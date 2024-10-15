# Python 2 Class - Week 2 - Assignment 3
# Scott Barren
#
#
# Description:
# Implement a basic queue using Python's built-in list data structure. The queue should support standard operations
# like enqueue, dequeue, and checking if the queue is empty.
# Instructions:
# Implement a class Queue with the following methods:
# enqueue(item): Adds an item to the end of the queue.
# dequeue(): Removes and returns the item at the front of the queue. If the queue is empty, it should raise an exception.
# is_empty(): Returns True if the queue is empty, False otherwise.
# size(): Returns the number of items in the queue.
#   Write a few test cases to demonstrate the functionality of the queue.
#
#
class Queue:
    def __init__(self):
        self.item = []  # Initialize an empty list to hold the queue items

    def enqueue(self, item):
        self.item.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("The Queue is EMPTY.  CANNOT Dequeue")
        item = self.item.pop(0)
        print(f"Dequeued: {item}")
        return item
    def is_empty(self):
        return len(self.item) == 0
    def size(self):
        return len(self.item)

Testing = Queue()
print("Is the Queue empty? ", Testing.is_empty())
Testing.enqueue(10)
Testing.enqueue(20)
Testing.enqueue(30)

print("Queue size: ", Testing.size())
print(Testing.dequeue())
print(Testing.dequeue())

print("Queue size: ", Testing.size())

print("Is the Queue empty? ", Testing.is_empty())