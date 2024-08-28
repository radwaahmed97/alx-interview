#!/usr/bin/python3
"""program that solves the N queens problem"""

import sys


def queens_recursion(N):
    """func recursion"""
    queens, result = [], []
    cols, diags1, diags2 = set(), set(), set()

    def back_track(row, N, queens):
        """backtracking func"""
        if row == N:
            result.append(queens[:])
            return
        for col in range(N):
            if (col in cols or row + col in diags1 or
                    row - col in diags2):
                continue
            cols.add(col)
            diags1.add(row + col)
            diags2.add(row - col)
            queens.append([row, col])
            back_track(row + 1, N, queens)

            cols.remove(col)
            diags1.remove(row + col)
            diags2.remove(row - col)
            queens.pop()
    back_track(0, N, queens)
    return result


def solve():
    """
    program solves the challenge of placing N non-attacking queens
    on an NxN chessboard
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N\n")
        sys.exit(1)
    else:
        N = sys.argv[1]
        if not N.isdigit():
            print("N must be a number")
            exit(1)
        elif int(N) < 4:
            print("N must be at least 4\n")
            sys.exit(1)
        else:
            possible_sols = queens_recursion(int(N))
            for sol in possible_sols:
                print(sol)


if __name__ == '__main__':
    solve()
