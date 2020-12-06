"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        d = {}
        node = head
        while node:
            cnode = Node(node.val)
            d[node] = cnode
            node = node.next
        node = head
        while node:
            if node.next:
                d[node].next = d[node.next]
            if node.random:
                d[node].random = d[node.random]
            node = node.next
        return d[head]