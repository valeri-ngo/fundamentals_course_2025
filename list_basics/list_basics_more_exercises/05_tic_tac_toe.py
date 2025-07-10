board = [list(map(int, input().split())) for _ in range(3)]

winner = 0

for row in board:
    if row[0] == row[1] == row[2] != 0:
        winner = row[0]

for i in range(3):
    if board[0][i] == board[1][i] == board [2][i] != 0:
        winner = board[0][i]

if board[0][0] == board [1][1] == board[2][2] != 0:
    winner = board[0][0]

if board[0][2] == board[1][1] == board[2][0] != 0:
    winner = board[0][2]

if winner == 1:
    print("First player won")
elif winner == 2:
    print("Second player won")
else:
    print("Draw!")