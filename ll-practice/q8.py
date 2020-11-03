"""
Write a function that removes a node with a given value 
from a singly-linked list. 
The function should take in two arguments:

node — the head of a linked list

value — a value that you want to remove

"""
def remove_node(node, value):
    current = node
    while current.next is not None:
        if current.next.data == value:
            current.next = current.next.next
            break
        current = current.next