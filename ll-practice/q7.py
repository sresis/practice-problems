"""
Write a function that takes in the head of a singly-linked list. 
It should return True if two nodes with the same data appear consecutively.

Example test cases:

in: 1 → 2 → 2
out: True

in: 1 → 2 → 1
out: False
"""
class LinkedList:
    def __init__(self, data):
        self.head = None
        self.tail = None

    def consec_data(self):
        """Return True if 2 nodes with same data appear consecutively."""
        current = self.head
        prev_val = None
        while current:
            if current == prev_val:
                return True
            prev_val = current
            current = current.next
        return False

