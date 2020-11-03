"""
Here’s a snippet from a linked list class:

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
Write a method for this class called print_list. 
It should print out the data for each node in the linked list and return None.

"""
class LinkedList:
    def __init__(self, data):
        self.head = None
        self.tail = None

    def print_list(self):
        """ Print the data for each node in LL."""
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. WOWZA!\n")
