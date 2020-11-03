"""
Here’s a snippet from a linked list class:

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
Write a method called print_odd_nodes that prints the nodes with 
odd-numbered indices (1, 3, 5, …, etc.)
"""
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def print_odd_nodes(self):
        """Print nodes with odd numbered indices."""
        counter = 0
        current = self.head
        while current:
            if counter / 2 != 0:
                print(current.data)
            current = current.next
            counter += 1
