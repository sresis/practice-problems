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
    def remove_dups(self):
        """Remove duplicate nodes.
            >>> ll = LinkedList()
            >>> ll.add_node('dog')
            >>> ll.add_node('cat')
            >>> ll.add_node('dog')
            >>> ll.add_node('fish')
        
            >>> ll.remove_dups()
            dog
            cat
            fish
        """
        seen_vals = []
        current_node = self.head.next
        print(current_node.prev.data)
            



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