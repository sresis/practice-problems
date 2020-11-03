"""
Here’s a snippet from a linked list class:

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
Write a method for this class called append. 
It should take in a node instance and add it to the end of the linked list.

Remember to account for appending to an empty list.
"""
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, node):
        if self.tail == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
