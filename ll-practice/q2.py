"""
Define two classes:

DblNode — a node in a doubly-linked list

DblLinkedList — a doubly-linked list with a head and tail

You are only required to define the __init__ method for each class.
"""
class DblNode(object):
    def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DblLinkedList(object):

    def __init__(self):
         self.head = None
         self.tail = None