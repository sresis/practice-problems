# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # go through each node
        # if it doesn't have a left node descendant, add its value to the count
        # use a stack
        
        if root is None:
            return 0
        def is_leaf(root):
            """Returns true if it has no children"""
            if root is not None and root.left is None and root.right is None:
                return True
            else:
                return False    
        node_stack = [root]
        total = 0
        while node_stack:
            sub_root = node_stack.pop()
            if is_leaf(sub_root.left):
                total += sub_root.left.val
            if sub_root.right is not None:
                node_stack.append(sub_root.right)
            if sub_root.left is not None:
                node_stack.append(sub_root.left)
        return total
                
            
        
        