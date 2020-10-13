class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList(object):
    """Linked List."""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
            """Add node with data to end of list."""

            new_node = Node(data)

            if self.head is None:
                self.head = new_node

            if self.tail is not None:
                self.tail.next = new_node

            self.tail = new_node        
    def return_k_node(self, k):
        """Remove duplicate nodes.
            >>> ll = LinkedList()
            >>> ll.add_node('dog')
            >>> ll.add_node('cat')
            >>> ll.add_node('dog')
            >>> ll.add_node('fish')
        
            >>> ll.return_k_node(2)
            'cat'
            >>> ll.return_k_node(4)
            'fish'
        """
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            if count == k:
                return current_node.data
            current_node = current_node.next
        
            



    # go through each node
    # keep track of what you've seen
    # if it isn't in there, keep going
    # if it is in seen list, set prev.next to n.next
if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()