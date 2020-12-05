# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # handle if empty
        if not root:
            return None
        ## stack to store
        stack = [root]
        while len(stack):
            ## get most recent in stack, then add left and right
            root = stack.pop()
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            ## now make root.left none
            root.left = None
            # most recent item in stack otherwise none
            root.right = stack[-1] if len(stack) else None
        
    