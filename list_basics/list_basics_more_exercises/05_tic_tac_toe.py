board = [list(map(int, input().split())) for _ in range(3)]


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != 0:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    return 0


winner = check_winner(board)

if winner == 1:
    print("First player won")
elif winner == 2:
    print("Second player won")
else:
    print("Draw!")
