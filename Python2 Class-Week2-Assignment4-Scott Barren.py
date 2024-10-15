# Python 2 Class - Week 2 - Assignment 4
# Scott Barren
#
# Description:
# Use Python's  collections.deque to implement a more efficient queue.
# Instructions:
# Implement a class  DequeQueue with the following methods:
# enqueue(item): Adds an item to the end of the queue.
# dequeue(): Removes and returns the item at the front of the queue. If the queue is empty,
# it should raise an exception.
# is_empty(): Returns True if the queue is empty, False otherwise.
# size(): Returns the number of items in the queue.
# Write a few test cases to demonstrate the functionality of the queue.
#
#
from collections import deque

class DequeQueue:
    def __init__(self):
        self.queue = deque()  # Initialize an empty deque for the queue

    def enqueue(self, item):
        self.queue.append(item)  # Add item to the end of the queue (right side)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue is not allowed.")
        item = self.queue.popleft()  # Remove item from the front of the queue (left side)
        print(f"Dequeued: {item}")
        return item

    def is_empty(self):
        return len(self.queue) == 0  # Returns True if the deque is empty

    def size(self):
        return len(self.queue)  # Returns the number of items in the queue

# Testing the DequeQueue
dq = DequeQueue()
print("Is the Queue empty? ", dq.is_empty())

# Enqueuing items
dq.enqueue(10)
dq.enqueue(20)
dq.enqueue(30)

# Checking the size
print("Queue size: ", dq.size())

# Dequeuing items
dq.dequeue()
dq.dequeue()

# Checking the size after dequeuing
print("Queue size: ", dq.size())

# Checking if the queue is empty
print("Is the Queue empty? ", dq.is_empty())

# Dequeue the last item and check again
dq.dequeue()
print("Is the Queue empty? ", dq.is_empty())

# Attempt to dequeue from an empty queue to demonstrate exception handling
try:
    dq.dequeue()
except IndexError as e:
    print(e)