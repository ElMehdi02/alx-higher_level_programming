import sys
"""Solves the N-queens puzzle"""

def nqueens(N):
    """ Check if N is an integer"""
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
        
    """ Check if N is at least 4 """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
        
    """ Initialize the board """
    board = [-1] * N

    """Recursive function to find all solutions """
    def place_queen(row, column):
        """ Check if the queen can be placed in this column """
        for i in range(row):
            if board[i] == column or \
               board[i] - i == column - row or \
               board[i] + i == column + row:
                return False
        return True
    
    def solve(row):
        if row == N:
            print(" ".join(str(i+1) for i in board))
            return
        for col in range(N):
            if place_queen(row, col):
                board[row] = col
                solve(row + 1)
                
    solve(0)

""" Check if the correct number of arguments is provided """
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

nqueens(sys.argv[1])
