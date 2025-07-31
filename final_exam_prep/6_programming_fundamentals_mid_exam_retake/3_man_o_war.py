def fire(warship: list, index: int, damage: int):
    if 0 <= index < len(warship):
        warship[index] -= damage
        if warship[index] <= 0:
            print('You won! The enemy ship has sunken.')
            return True
    return False

def defend(pirate_ship: list, start: int, end: int, damage: int):
    if 0 <= start <= end < len(pirate_ship):
        for damage_taken in range(start, end +1):
            pirate_ship[damage_taken] -= damage
            if pirate_ship[damage_taken] <= 0:
                print('You lost! The pirate ship has sunken.')
                return True
    return False

def repair(pirate_ship: list, index: int, health: int, maximum_hp_capacity: int):
    if 0 <= index < len(pirate_ship):
        pirate_ship[index] += health
        if pirate_ship[index] > maximum_hp_capacity:
            pirate_ship[index] = maximum_hp_capacity

def status(pirate_ship: list, maximum_hp_capacity):
    threshold = 0.2 * maximum_hp_capacity
    count = 0
    for section in pirate_ship:
        if section < threshold:
            count += 1
    print(f"{count} sections need repair.")

def main():

    pirate_ship = list(map(int, input().split('>')))
    warship = list(map(int, input().split('>')))
    maximum_hp_capacity = int(input())

    sunken_ship = False

    while True:
        command = input()

        if command== "Retire":
            break

        split_command = command.split()

        action = split_command[0]

        if action == 'Fire':
            index, damage = int(split_command[1]), int(split_command[2])
            if fire(warship, index, damage):
                sunken_ship = True
                break
        elif action == 'Defend':
            start, end, damage = int(split_command[1]), int(split_command[2]), int(split_command[3])
            if defend(pirate_ship, start, end, damage):
                sunken_ship = True
                break
        elif action == 'Repair':
            index, health = int(split_command[1]), int(split_command[2])
            repair(pirate_ship, index, health, maximum_hp_capacity)
        elif action == 'Status':
            status(pirate_ship, maximum_hp_capacity)
    if not sunken_ship:
        print(f"Pirate ship status: {sum(pirate_ship)}")
        print(f"Warship status: {sum(warship)}")

if __name__ == '__main__':
    main()