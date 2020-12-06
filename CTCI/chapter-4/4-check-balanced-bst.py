# Tell whether or not a binary tree is balanced.

def is_balanced(binary_tree):
    if binary_tree is None:
        return (True, 0)
    (left_balanced, left_depth) = is_balanced(binary_tree.left)
    if left_balanced == False:
        return (False, None)
    (right_balanced, right_depth) = is_balanced(binary_tree.right)
    # check if right is balanced OR right/left diff is 1 or less
    if right_balanced == False or abs(right_depth - left_depth) > 1:
        return (False, None)
    # add 1 to include head
    depth = max(right_depth, left_depth) + 1
    return (True, depth)
class Node():
  def __init__(self, left=None, right=None):
    self.left, self.right = left, right

import unittest

class Test(unittest.TestCase):
  def test_is_balanced(self):
    self.assertEqual(is_balanced(Node(Node(),Node())), (True, 2))
    self.assertEqual(is_balanced(Node(Node(),Node(Node()))), (True, 3))
    self.assertEqual(is_balanced(Node(Node(),Node(Node(Node())))),
        (False, None))
    self.assertEqual(is_balanced(Node(Node(Node()),Node(Node(Node())))),
        (False,None))
    self.assertEqual(is_balanced(Node(Node(Node()),
        Node(Node(Node()),Node()))), (True, 4))

if __name__ == "__main__":
  unittest.main()
