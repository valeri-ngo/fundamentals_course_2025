def find_kate(maze):
    for i, row in enumerate(maze):
        if 'k' in row:
            return [i, row.index('k')]
    return None

def is_edge(pos, rows, cols):
    return pos[0] == 0 or pos[0] == rows - 1 or pos[1] == 0 or pos[1] == cols - 1

def find_moves(pos, maze):
    moves = []
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dx, dy in directions:
        new_x, new_y = pos[0] + dx, pos[1] + dy
        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]):
            if maze[new_x][new_y] == ' ':
                moves.append([new_x, new_y])
    return moves

def kate_escape(maze, start):
    visited = [start]
    path = [start]
    maze[start[0]][start[1]] = ' '
    steps = 0
    max_steps = -1

    while path:
        current = path[-1]

        if is_edge(current, len(maze), len(maze[0])):
            max_steps = max(max_steps, len(path) - 1)

        next_moves = find_moves(current, maze)
        moved = False

        for move in next_moves:
            if move not in visited:
                visited.append(move)
                path.append(move)
                steps += 1
                moved = True
                break

        if not moved:
            # Dead end
            maze[current[0]][current[1]] = '@'
            path.pop()
            steps -= 1

    return max_steps + 1 if max_steps != -1 else -1

n = int(input())
maze = [list(input()) for _ in range(n)]

start_pos = find_kate(maze)
if not start_pos:
    print("Kate cannot get out")
else:
    result = kate_escape(maze, start_pos)
    if result == -1:
        print("Kate cannot get out")
    else:
        print(f"Kate got out in {result} moves")
