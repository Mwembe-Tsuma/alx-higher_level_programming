#!/usr/bin/python3
""""Solves the N-queens puzzle."""


import sys

def nqueens(N):
    """Check if N is an int"""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    """Checking if N is at least 4"""
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def x_safe(board, row, col):
        """X out spots on a chessboard

        Args:
            board (list): The current working chessboard.
            row (int): The row.
            col (int): The column.
        """
        for x in range(row):
            if board[x] == col:
                return (False)

        x = row - 1
        y = col - 1
        while x >= 0 and y >= 0:
            if board[x] == y:
                return (False)
            x -= 1
            y -= 1

        x = row - 1
        y = col + 1
        while x >= 0 and y < N:
            if board[x] == y:
                return (False)
            x -= 1
            y += 1

        return (True)

    def get_solution(board, row):
        """Return list of lists rep of a solved chessboard"""
        if row == N:
            copy_board(board)
            return

        for col in range(N):
            if x_safe(board, row, col):
                board[row] = col
                get_solution(board, row + 1)

    def copy_board(board):
        for x in range(N):
            row_string = ""
            for y in range(N):
                if board[x] == y:
                    row_string += "Q "
                else:
                    row_string += ". "
            print(row_string.strip())
        print()

    board = [-1] * N
    get_solution(board, 0)

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
    nqueens(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)
