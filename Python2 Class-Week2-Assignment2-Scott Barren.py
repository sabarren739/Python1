# Python 2 Class - Week 2 - Assignment 2
# Scott Barren
#
# Removing a Node from a Singly Linked List
# ====================================
# Task: Implement a method remove(data) in the LinkedList class that removes the first occurrence of a node with
# the specified data from the list.
#
#
class Node:
    def __init__(self, data):
        self.data = data  # storing data
        self.next = None  # This is a next node pointer
class SinglyLinkedList:
    def __init__(self):
        self.head = None  #Initialize the head of the list
    def append(self, data):
        new_node = Node(data) #Create the node
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  #Traverse to the end of the list
            last_node = last_node.next
        last_node.next = new_node # Link last node to the new node
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head  #Link the new node to the current head
        self.head = new_node  #update the head to the new node
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def remove(self, data):
        # If the list is empty then there's nothing to remove
        if not self.head:
            return
        # If the head contains the data to be removed
        if self.head.data == data:
            self.head = self.head.next  # Update head to next node
            return

        # Traverse the list to find the node to remove
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next  # Bypass the node to be removed
                return
            current_node = current_node.next

if __name__ == "__main__":
    linkedlist = SinglyLinkedList()
    linkedlist.append(10)
    linkedlist.append(20)
    linkedlist.append(30)
    linkedlist.prepend(5)
    linkedlist.prepend(1)
    linkedlist.print_list()  # Output: 1 -> 5 -> 10 -> 20 -> 30 -> None

    linkedlist.remove(10)
    linkedlist.print_list()  # Output: 1 -> 5 -> 20 -> 30 -> None

    linkedlist.remove(1)
    linkedlist.print_list()  # Output: 5 -> 20 -> 30 -> None

    linkedlist.remove(30)
    linkedlist.print_list()  # Output: 5 -> 20 -> None