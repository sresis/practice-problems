"""
Write a function that takes in the head of a singly-linked list. 
It should return the head of a linked list with the nodes 
in reversed order.
"""
def reverse_ll(node):
    # use a stack to store all nodes
    stack = []
    current = node
    while current is not None:
        stack.append(current)
        current = current.next
    # nodes will be popped in reverse order
    reversed_ll = stack.pop()
    current = reversed_ll
    while len(stack) != 0:
        current.next = stack.pop()
        current = current.next
    return reversed_ll