class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        root = self.root
        if not root:
            self.root = Node(val)
            return self.root
        while root:
            if root.info < val:
                # either move on to right node, or if right node doesn't exist, add it
                if root.right is not None:
                    root = root.right
                else:
                    root.right = Node(val)
                    break
            elif root.info > val:
                if root.left is not None:
                    root = root.left
                else:
                    root.left = Node(val)
                    break
            

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
