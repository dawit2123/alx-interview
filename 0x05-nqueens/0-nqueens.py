#!/usr/bin/python3
"""N queens solution finder module."""
import sys


def print_usage():
    """Prints the usage message and exits the program."""
    print("Usage: nqueens N")
    sys.exit(1)


def validate_input():
    """Validates and retrieves the input for the N-Queens problem.

    Returns:
        int: The size of the chessboard (N).
    """
    if len(sys.argv) != 2:
        print_usage()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def is_safe(queens, row, col):
    """Checks if a queen can be safely placed on the board.

    Args:
        queens (list): A list representing the positions of queens.
        row (int): The current row to place the queen.
        col (int): The column to place the queen.

    Returns:
        bool: True if the queen can be placed safely, False otherwise.
    """
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n):
    """Solves the N queens problem and prints all solutions.

    Args:
        n (int): The size of the chessboard (N).
    """
    def backtrack(row, queens):
        """Recursive backtracking to find all solutions.

        Args:
            row (int): The current row to place the queen.
            queens (list): A list representing the positions of queens.
        """
        if row == n:
            # If all queens are placed, print the solution
            solution = [[r, c] for r, c in enumerate(queens)]
            solutions.append(solution)
            return

        for col in range(n):
            if is_safe(queens, row, col):
                queens.append(col)
                backtrack(row + 1, queens)
                queens.pop()

    solutions = []
    backtrack(0, [])
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    n = validate_input()
    solve_nqueens(n)
