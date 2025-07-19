def battle_ships(maze):
    destroyed_ships = 0
    attacks = input().split()
    for attack in attacks:
        row, col = map(int,attack.split('-'))
        if maze[row][col] > 0:
            maze[row][col] -= 1
            if maze[row][col] <= 0:
                destroyed_ships += 1
    return destroyed_ships

number_of_rows = int(input())
matrix = [list(map(int, input().split())) for _ in range(number_of_rows)]

result = battle_ships(matrix)
print(result)