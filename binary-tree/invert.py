def invertBinaryTree(tree):
	queue = [tree]
	while len(queue):
		curr = queue.pop(0)
		if curr is None:
			continue
		swap(curr)
		queue.append(curr.left)
		queue.append(curr.right)
			

def swap(tree):
	tree.left, tree.right = tree.right, tree.left
		


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
