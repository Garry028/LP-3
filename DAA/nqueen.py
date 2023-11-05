def solveNQueens(n, initial_queen_position):
    col = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = [["."]*n for i in range(n)]

    initial_row, initial_col = initial_queen_position
    board[initial_row][initial_col] = "Q"
    col.add(initial_col)
    posDiag.add(initial_row + initial_col)
    negDiag.add(initial_row - initial_col)

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = "Q"

            backtrack(r+1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = "."

    # Start from the next row after placing the initial queen
    backtrack(initial_row + 1)
    return res


# Ask the user for the initial queen's position
initial_row = int(
    input("Enter the initial row for the first queen (0 to 7): "))
initial_col = int(
    input("Enter the initial column for the first queen (0 to 7): "))
initial_queen_position = (initial_row, initial_col)

solutions = solveNQueens(8, initial_queen_position)

for solution in solutions:
    for row in solution:
        print(" ".join(row))
    print()

# TC --> O(N!) worst case
# SC --> O(N)