def is_valid(row, col, matrix_, visited_):
    if 0 <= row < len(matrix_) and 0 <= col < len(matrix_[0]):
        if matrix_[row][col] == '.' and not visited_[row][col]:
            return True
    return False

def dfs(row, col, matrix_, visited_):
    visited_[row][col] = True
    count = 1

    for dr, dc in directions.values():
        new_row = row + dr
        new_col = col + dc
        if is_valid(new_row, new_col, matrix_, visited_):
            count += dfs(new_row, new_col, matrix_, visited_)
    return count

directions = {'up': (-1, 0),
              'down': (1, 0),
              'left': (0, -1),
              'right': (0, 1)}

number = int(input())
matrix = [input().split() for _ in range(number)]

visited = [[False for _ in range(len(matrix[0]))] for _ in range(number)]

max_count = 0

for row in range(number):
    for col in range(len(matrix[0])):
        if is_valid(row, col, matrix, visited):
            connected = dfs(row, col, matrix, visited)
            max_count = max(max_count, connected)

print(max_count)