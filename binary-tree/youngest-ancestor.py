# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	# get depths of each descendant
	depth1 = get_depth(topAncestor, descendantOne)
	depth2 = get_depth(topAncestor, descendantTwo)
	# iterate until they match depth
	if depth1 > depth2:
		while depth1 > depth2:
			depth1 -= 1
			descendantOne = descendantOne.ancestor
	elif depth2 > depth1:
		while depth2 > depth1:
			depth2 -= 1
			descendantTwo = descendantTwo.ancestor
	# now continue until we get matching
	while descendantOne != descendantTwo:
		descendantOne = descendantOne.ancestor
		descendantTwo = descendantTwo.ancestor
	return descendantOne
		
	
def get_depth(top, descendant):
	"""Returns the deoth of a descendent"""
	depth = 0
	while top != descendant:
		depth += 1
		descendant = descendant.ancestor
	return depth
