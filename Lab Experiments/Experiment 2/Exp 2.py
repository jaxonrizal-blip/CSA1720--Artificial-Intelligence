
def solve(board, row, n):
    if row == n:
        for r in board:
            print(" ".join("Q" if x else "." for x in r))
        return True

    for col in range(n):
        safe = True

        for r in range(row):
            if (board[r][col] == 1 or
                abs(board[r].index(1) - col) == row - r):
                safe = False
                break

        if safe:
            board[row][col] = 1
            if solve(board, row + 1, n):
                return True
            board[row][col] = 0

    return False

n = int(input("Enter number of queens: "))
board = [[0] * n for _ in range(n)]

if not solve(board, 0, n):
    print("No solution exists")
