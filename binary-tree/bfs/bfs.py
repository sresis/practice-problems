# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # use a queue
		# then pop.(0)
		to_visit = []
		names = []
		curr = self
		while curr:
			names.append(curr.name)
			to_visit.extend(curr.children)
			if to_visit != []:
				next_node = to_visit.pop(0)
				curr = next_node
			else:
				curr = None
		return names
			 