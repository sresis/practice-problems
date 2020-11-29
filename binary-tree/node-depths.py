def nodeDepths(root):
	depths = []
	total = 0
	get_node_depths(root, 0, depths)
	# return sum of each depth
	for item in depths:
		total += item
	return total 
    
def get_node_depths(node, curr_depth, depths):
	if node is None:
		return
	
	depths.append(curr_depth)
	new_depth = curr_depth + 1
	# when you get to end, reset new depth
	if node.right is None and node.left is None:
		new_depth = 0
	get_node_depths(node.left, new_depth, depths)
	get_node_depths(node.right, new_depth, depths)
		
	


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
