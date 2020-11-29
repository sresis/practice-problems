# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	sums = []
	calc_branch_sums(root, 0, sums)
	return sums

def calc_branch_sums(node, curr_sum, sums):
	if node is None:
		return
	new_sum = curr_sum + node.value
	# check if no children
	if node.left is None and node.right is None:
		sums.append(new_sum)
		return
	calc_branch_sums(node.left, new_sum, sums)
	calc_branch_sums(node.right, new_sum, sums)
	
	
