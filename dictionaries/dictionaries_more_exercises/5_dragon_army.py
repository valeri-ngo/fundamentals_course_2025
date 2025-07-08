dragons_dict = {}
number_of_dragons = int(input())

for numbers in range(number_of_dragons):

    default_damage = 45
    default_health = 250
    default_armor = 10

    line_input = input()

    dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor = line_input.split(" ")
    if dragon_damage == "null":
        dragon_damage = default_damage
    else:
        dragon_damage = int(dragon_damage)
    if dragon_health == "null":
        dragon_health = default_health
    else:
        dragon_health = int(dragon_health)
    if dragon_armor == "null":
        dragon_armor = default_armor
    else:
        dragon_armor = int(dragon_armor)
    stats = {'damage': dragon_damage,
         'health': dragon_health,
         'armor': dragon_armor
         }
    if (dragon_type, dragon_name) not in dragons_dict:
        dragons_dict[(dragon_type, dragon_name)] = stats
    else:
        dragons_dict[(dragon_type, dragon_name)] = stats

grouped_dragons = {}

for (dragon_type, dragon_name), stats in dragons_dict.items():
    if dragon_type not in grouped_dragons:
        grouped_dragons[dragon_type] = {}
    grouped_dragons[dragon_type][dragon_name] = stats

for dragon_type, dragons in grouped_dragons.items():
    current_dragon = grouped_dragons[dragon_type]
    total_damage = 0
    total_health = 0
    total_armor = 0
    count_dragons = len(current_dragon)
    for dragon_name, stats in dragons.items():
        total_damage += stats['damage']
        total_health += stats['health']
        total_armor += stats['armor']

    average_damage = total_damage / count_dragons
    average_health = total_health / count_dragons
    average_armor = total_armor / count_dragons
    print(f"{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    for dragon_name in sorted(dragons):
        stats = dragons[dragon_name]
        print(f"-{dragon_name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")
