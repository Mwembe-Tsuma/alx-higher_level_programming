#!/usr/bin/python3
"""Solves the N-queens puzzle."""

import sys


def init_chessboard(n):
    """Initialize a chessboard with 0's."""
    board = []
    [board.append([]) for x in range(n)]
    [row.append(' ') for x in range(n) for row in board]
    return (board)


def board_copy(board):
    """Return a copy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_copy, board))
    return (board)


def solve(board):
    """Return list of lists rep of a solved chessboard."""
    solution = []
    for rows in range(len(board)):
        for cols in range(len(board)):
            if board[rows][cols] == "Q":
                solution.append([rows, cols])
                break
    return (solution)


def print_out(board, row, col):
    """Print X out spots on a chessboard.

    Args:
        board (list): The current chessboard.
        row (int): The row
        col (int): The column
    """
    for cols in range(col + 1, len(board)):
        board[row][cols] = "x"
    for cols in range(col - 1, -1, -1):
        board[row][cols] = "x"
    for rows in range(row + 1, len(board)):
        board[rows][col] = "x"
    for rows in range(row - 1, -1, -1):
        board[rows][col] = "x"
    cols = col + 1
    for rows in range(row + 1, len(board)):
        if cols >= len(board):
            break
        board[rows][cols] = "x"
        cols += 1
    cols = col - 1
    for rows in range(row - 1, -1, -1):
        if cols < 0:
            break
        board[rows][cols]
        cols -= 1
    cols = col + 1
    for rows in range(row - 1, -1, -1):
        if cols >= len(board):
            break
        board[rows][cols] = "x"
        cols += 1
    cols = col - 1
    for rows in range(row + 1, len(board)):
        if cols < 0:
            break
        board[rows][cols] = "x"
        cols -= 1


def recursive_solution(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current chessboard.
        row (int): The row.
        queens (int): The number of placed queens.
        solutions (list): A list of lists of solutions.
    """
    if queens == len(board):
        solutions.append(solve(board))
        return (solutions)

    for cols in range(len(board)):
        if board[row][cols] == " ":
            temp_board = board_copy(board)
            temp_board[row][cols] = "Q"
            print_out(temp_board, row, cols)
            solutions = recursive_solution(temp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_chessboard(int(sys.argv[1]))
    solutions = recursive_solution(board, 0, 0, [])
    for i in solutions:
        print(i)
