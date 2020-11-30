def minHeightBst(array):
    return create_bst(array, 0, len(array)-1)
def create_bst(array, start, end):
	if end < start:
		return None
	mid = (start + end) // 2
	val = array[mid]
	bst = BST(val)
	bst.left = create_bst(array, start, mid-1)
	bst.right = create_bst(array, mid + 1, end)
	return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
