class BinarySearchNode(object):
    """Binary tree node."""

    def __init__(self, data, left=None, right=None):
        self.data = data

        self.left = left
        self.right = right

    def __repr__(self):
        """Debugging-friendly representation."""

        return "<BinaryNode %s>" % self.data

    def find_iterative(self, sought):
        """Return node with this data.

        Start here. Return None if not found.

        >>> root_left_left_left = BinarySearchNode(1)
        >>> root_left_left = BinarySearchNode(2, root_left_left_left)
        >>> root_left_right = BinarySearchNode(4)
        >>> root_left = BinarySearchNode(3, root_left_left, root_left_right)
        >>> root_right_right_left = BinarySearchNode(8)
        >>> root_right_right_right = BinarySearchNode(10)
        >>> root_right_left = BinarySearchNode(6)
        >>> root_right_right = BinarySearchNode(9,root_right_right_left, root_right_right_right)
        >>> root_right = BinarySearchNode(7, root_right_left, root_right_right)
        >>> root_node = BinarySearchNode(5, root_left, root_right)
        >>> root_node.find_iterative(7)
        <BinaryNode 7>
        >>> root_node.find_iterative(11) is None
        True
        >>> root_node.find_iterative(0) is None
        True
        """

    def find_recursive(self, sought):
        """Return node with this data.

        Start here. Return None if not found.

        >>> root_left_left_left = BinarySearchNode(1)
        >>> root_left_left = BinarySearchNode(2, root_left_left_left)
        >>> root_left_right = BinarySearchNode(4)
        >>> root_left = BinarySearchNode(3, root_left_left, root_left_right)
        >>> root_right_right_left = BinarySearchNode(8)
        >>> root_right_right_right = BinarySearchNode(10)
        >>> root_right_left = BinarySearchNode(6)
        >>> root_right_right = BinarySearchNode(9,root_right_right_left, root_right_right_right)
        >>> root_right = BinarySearchNode(7, root_right_left, root_right_right)
        >>> root_node = BinarySearchNode(5, root_left, root_right)
        >>> root_node.find_recursive(7)
        <BinaryNode 7>
        >>> root_node.find_recursive(11) is None
        True
        >>> root_node.find_recursive(0) is None
        True
        """
        if self.data == sought:
            return sought
        elif self.data > sought and self.left is not None:
            return find_recursive(self.left, sought)
        elif self.data < sought and self.right is not None:
            return find_recursive(self.right, sought)
        else:
            return None


    def insert_iterative(self, data):
        """Insert node in its right spot, assuming there are no ties.

        Note: this is not optimized and will not keep the tree balanced.

        >>> root_left_left = BinarySearchNode(1, None)
        >>> root_left_right = BinarySearchNode(4)
        >>> root_left = BinarySearchNode(3, root_left_left, root_left_right)
        >>> root_right_right_left = BinarySearchNode(8)
        >>> root_right_right_right = BinarySearchNode(10)
        >>> root_right_right = BinarySearchNode(9,root_right_right_left, root_right_right_right)
        >>> root_right = BinarySearchNode(7, None, root_right_right)
        >>> root_node = BinarySearchNode(5, root_left, root_right)
        >>> root_node.insert_recursive(11)
        >>> root_node.right.right.right.right
        <BinaryNode 11>
        >>> root_node.insert_recursive(6)
        >>> root_node.right.left
        <BinaryNode 6>
        >>> root_node.insert_recursive(2)
        >>> root_node.left.left
        <BinaryNode 1>
        >>> root_node.left.left.right
        <BinaryNode 2>
        """



    def insert_recursive(self, data):
        """Insert new node with `new_data` to BST tree rooted here.

        >>> root_left_left = BinarySearchNode(1, None)
        >>> root_left_right = BinarySearchNode(4)
        >>> root_left = BinarySearchNode(3, root_left_left, root_left_right)
        >>> root_right_right_left = BinarySearchNode(8)
        >>> root_right_right_right = BinarySearchNode(10)
        >>> root_right_right = BinarySearchNode(9,root_right_right_left, root_right_right_right)
        >>> root_right = BinarySearchNode(7, None, root_right_right)
        >>> root_node = BinarySearchNode(5, root_left, root_right)
        >>> root_node.insert_recursive(11)
        >>> root_node.right.right.right.right
        <BinaryNode 11>
        >>> root_node.insert_recursive(6)
        >>> root_node.right.left
        <BinaryNode 6>
        >>> root_node.insert_recursive(2)
        >>> root_node.left.left
        <BinaryNode 1>
        >>> root_node.left.left.right
        <BinaryNode 2>
        """

        if data >= self.data:
            if self.right is None:
                self.right = BinarySearchNode(data)
            else:
                self.right.insert_recursive(data)
        else:
            if self.left is None:
                self.left = BinarySearchNode(data)
            else:
                self.left.insert_recursive(data)

    def count_total_nodes_iterative(self):
        """Count the overal number of nodes

        >>> root_left_left_left = BinarySearchNode(1)
        >>> root_left_left = BinarySearchNode(2, root_left_left_left)
        >>> root_left_right = BinarySearchNode(4)
        >>> root_left = BinarySearchNode(3, root_left_left, root_left_right)
        >>> root_right_right_left = BinarySearchNode(8)
        >>> root_right_right_right = BinarySearchNode(10)
        >>> root_right_left = BinarySearchNode(6)
        >>> root_right_right = BinarySearchNode(9,root_right_right_left, root_right_right_right)
        >>> root_right = BinarySearchNode(7, root_right_left, root_right_right)
        >>> root_node = BinarySearchNode(5, root_left, root_right)
        >>> total = root_node.count_total_nodes_iterative()
        >>> total == 10
        True
        """

 

    def count_total_nodes_recursive(self):
        """Count the overal number of nodes


        >>> root_left_left_left = BinarySearchNode(1)
        >>> root_left_left = BinarySearchNode(2, root_left_left_left)
        >>> root_left_right = BinarySearchNode(4)
        >>> root_left = BinarySearchNode(3, root_left_left, root_left_right)
        >>> root_right_right_left = BinarySearchNode(8)
        >>> root_right_right_right = BinarySearchNode(10)
        >>> root_right_left = BinarySearchNode(6)
        >>> root_right_right = BinarySearchNode(9,root_right_right_left, root_right_right_right)
        >>> root_right = BinarySearchNode(7, root_right_left, root_right_right)
        >>> root_node = BinarySearchNode(5, root_left, root_right)
        >>> total = root_node.count_total_nodes_recursive()
        >>> total == 10
        True
        """
