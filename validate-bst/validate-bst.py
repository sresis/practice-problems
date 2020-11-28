# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
	def helper(tree, min_val, max_val):
		if tree is None:
			return True
		if tree.value < min_val or tree.value >= max_val:
			return False
		left_is_valid = helper(tree.left, min_val, tree.value)
		return left_is_valid and helper(tree.right, tree.value, max_val)

	return helper(tree, float("-inf"), float("inf"))
    
	