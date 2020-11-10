"""
    >>> queensAttacktheKing([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], [0,0])
    [[1, 0], [0, 1], [3, 3]]
"""
def queensAttacktheKing(queens, king):
    ## identify each direction the queen can be from the king
    ## row-left, row-right, col-up, col-down, ur-diag, dr-diag, ul-diag, ur-diag
    ## [[-1, 0], [1, 0], [0,-1], [0,1], [1, -1], [1, 1], [-1, -1], [-1, 1]]
    
    ## for each direction... keep adding to king value until either one queen is found OR edge is               reached
        ## if queen is found, append it to danger_queens and break
    
    directions = [[-1, 0], [1, 0], [0,-1], [0,1], [1, -1], [1, 1], [-1, -1], [-1, 1]]
    k_row = king[0]
    k_col = king[1]
    danger_queens = []
    # start at king col
    for direction in directions:
        row = k_row
        col = k_col
        while row < 8 and row >= 0 and col < 8 and col >= 0:
            row += direction[0]
            col += direction[1]
            if [row, col] in queens:
                danger_queens.append([row, col])
                break
            
    return danger_queens

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
