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
            if self.head is None:
                return
            current = self.head
            x = current
            while current:
                runner = current
                while runner.next:
                    if runner.next.data == current.data:
                        runner.next = runner.next.next
                    else:
                        runner = runner.next
                current = current.next
            while x:
                print(x.data)
                x = x.next


if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()