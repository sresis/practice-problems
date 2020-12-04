# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        # if it is less than target, only look at right
        # if it is > target, only look at left
        closest = root.val
        while root is not None:
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return closest