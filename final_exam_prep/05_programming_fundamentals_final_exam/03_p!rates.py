def plunder(city_info: dict, town: str, people_killed: int, gold_plundered: int) -> list:
    pass
def prosper(city_info: dict, town: str, treasure: int) -> list:
    pass

is_sail = False
city_info = {}

while True:
    data_input = input()

    if data_input == 'Sail':
        is_sail = True
        break

    town, population, gold = data_input.split('||')

    if town not in city_info:
        city_info[town] = {'population': int(population),
                            'gold': int(gold)}
    else:
        city_info[town]['population'] += int(population)
        city_info[town]['gold'] += int(gold)

while is_sail:
    command = input()
    if command == 'End':
        break
    split_into_parts = command.split('=>')
    if split_into_parts[0] == 'Plunder':
        city, killed_people, plundered_gold = split_into_parts[1], int(split_into_parts[2]), int(split_into_parts[3])
        plunder(city_info, city, killed_people, plundered_gold)
    elif split_into_parts[0] == 'Prosper':
        city, gold_added = split_into_parts[1], int(split_into_parts[2])
        prosper(city_info, city, gold_added)