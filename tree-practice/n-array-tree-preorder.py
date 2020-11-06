from typing import List
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
          def dfs(node, result):
            if not node:
                return
            
            result.append(node.val)
            for child in node.children:
                dfs(child, result)
        result = []
        dfs(root, result)
        
        return result

Solution.preorder([1,None,3,2,4,None,5,6])