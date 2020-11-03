"""Define two classes:

Node — a node in a singly-linked list

LinkedList — a singly-linked list with a head and tail.

You are only required to define the __init__ method for each class.
"""
class Node(object):

     def __init__(self, data, next=None):
         self.data = data
         self.next = None

class LinkedList(object):

    def __init__(self):
         self.head = None
         self.tail = None

