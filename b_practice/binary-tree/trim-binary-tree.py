# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # if we get to one that is less than low, only consider its right children
        # if we get to one that is > high, only consider its left children
        # otherwise, consider both children
        def trim(node):
            """ trims the node"""
            if node == None:
                return None
            elif node.val < low:
                return trim(node.right)
            elif node.val > high:
                return trim(node.left)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
        return trim(root)