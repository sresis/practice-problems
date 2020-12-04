# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            mid = (left_idx + right_idx) // 2
            print(mid)
            root = TreeNode(nums[mid])
            root.left = helper(left_idx, mid - 1)
            root.right = helper(mid + 1, right_idx)
            return root
            
        return helper(0, len(nums)-1)
            