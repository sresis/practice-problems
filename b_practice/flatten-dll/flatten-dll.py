"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head):
        if not head:
            return
        ## set this temp value before the head
        temp = Node(0, None, head, None)
        # use stack to keep track of nodes to visit/flatten
        stack = []
        stack.append(head)
        prev = temp
        
        while stack:
            # get recent item in stack
            root = stack.pop()
            # update the values
            root.prev = prev
            prev.next = root
            # add the next value to stack
            if root.next:
                stack.append(root.next)
                root.next = None
            ## then add child. handle first in stack
            if root.child:
                stack.append(root.child)
                root.child = None
            prev = root
        ## set temp
        temp.next.prev = None
        return temp.next
                
        
                
         