def has_energy(current_energy: int, distance: int) -> bool:
    return current_energy >= distance

def won_battles(battle_count: int) -> tuple:
    battle_count += 1
    added_energy = battle_count if battle_count % 3 == 0 else 0
    return battle_count, added_energy

initial_energy = int(input())
battle_count = 0

while True:
    command_or_distance = input()

    if command_or_distance == 'End of battle':
        print(f"Won battles: {battle_count}. Energy left: {initial_energy}")
        break

    else:
        distance = int(command_or_distance)

    if has_energy(initial_energy, distance):
        initial_energy -= distance
        battle_count, bonus_energy = won_battles(battle_count)
        initial_energy += bonus_energy

    else:
        print(f'Not enough energy! Game ends with {battle_count} won battles and {initial_energy} energy')
        break