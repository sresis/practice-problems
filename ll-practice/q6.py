"""
Here’s a snippet from a doubly-linked list class:

class DblLinkedList
    def __init__(self):
        self.head = None
        self.tail = None
Write a method for this class called remove. It should take in a node instance and remove it from the list.
"""
class DblLinkedList
    def __init__(self):
        self.head = None
        self.tail = None
    def remove(self, node):
        """removes node from list."""
    
        if node.prev is None:
            self.head = node.next
        elif node.next is None:
            self.tail = node.prev
        else:
            node.prev.next = node.next

