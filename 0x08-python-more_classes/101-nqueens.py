#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col] == 1:
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False
        if col + (row - i) < N and board[i][col + (row - i)] == 1:
            return False
    return True


def solve_nqueens(board, row, N, solutions):
    if row == N:
        solutions.append([[r, c] for r, c in enumerate(board)])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, row + 1, N, solutions)
            board[row][col] = 0


def print_solutions(solutions):
    for solution in solutions:
        print(solution)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    solve_nqueens(board, 0, N, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
