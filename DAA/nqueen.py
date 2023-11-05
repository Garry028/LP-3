def solveNQueens(n, initial_queen_position):
    def is_valid(board, row, col):
        # Check the column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check the upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # Check the upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False

        return True

    def backtrack(row):
        if row == n:
            res.append(["".join(row) for row in board])
            return

        for col in range(n):
            if (row, col) == initial_queen_position:
                continue  # Skip the specified initial position

            if is_valid(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    initial_row, initial_col = initial_queen_position
    res = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0)

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
        print(row)
    print()
