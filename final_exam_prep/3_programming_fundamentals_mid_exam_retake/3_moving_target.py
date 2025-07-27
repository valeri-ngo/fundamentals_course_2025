def shoot(targets: list[int], index: int, power: int) -> bool:
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
        return True
    return False

def add(targets: list[int], index: int, value: int) -> bool:
    if 0 <= index < len(targets):
        targets.insert(index, value)
        return True
    else:
        print('Invalid placement!')
        return False

def strike(targets: list[int], index: int, radius: int) -> bool:
    starting_index = index - radius
    ending_index = index + radius
    if starting_index >= 0 and ending_index < len(targets):
        del targets[starting_index:ending_index + 1]
        return True
    else:
        print('Strike missed!')
        return False

def main():
    targets = list(map(int, input().split()))
    shot_count = 0

    while True:
        command = input()
        if command == 'End':
            break

        split_command = command.split()
        action = split_command[0]

        if action == 'Shoot':
            index, power = int(split_command[1]), int(split_command[2])
            if shoot(targets, index, power):
                shot_count += 1

        elif action == 'Add':
            index = int(split_command[1])
            value = int(split_command[2])
            add(targets, index, value)

        elif action == 'Strike':
            index = int(split_command[1])
            radius = int(split_command[2])
            strike(targets, index, radius)

    print('|'.join(map(str, targets)))

if __name__ == '__main__':
    main()