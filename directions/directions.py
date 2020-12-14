"""
    >>> return_directions(['NORTH', 'SOUTH', 'NORTH', 'WEST'])
    ['NORTH', 'WEST']
    >>> return_directions(["NORTH","EAST","WEST","SOUTH","WEST","SOUTH","NORTH","WEST"])
    ['WEST', 'WEST']
"""

def return_directions(directions): 
    """Returns list of directions removing duplicates."""
    pairs = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    stack = []
    for i in range(len(directions)):
        if not stack or stack[-1] != pairs[directions[i]]:
            stack.append(directions[i])
        else:
            stack.pop()
        
    return stack



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. WOWZA!\n")
