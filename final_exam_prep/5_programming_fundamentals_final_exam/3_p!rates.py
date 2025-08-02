def plunder(city_info: dict, city: str, people_killed: int, gold_plundered: int) -> None:
    city_info[city]['population'] -= people_killed
    city_info[city]['gold'] -= gold_plundered
    print(f"{city} plundered! {gold_plundered} gold stolen, {people_killed} citizens killed.")

    if city_info[city]['population'] <= 0 or city_info[city]['gold'] <= 0:
        del city_info[city]
        print(f'{city} has been wiped off the map!')

def prosper(city_info: dict, town: str, gold_added: int) -> None:

    if gold_added < 0:
        print(f'Gold added cannot be a negative number!')
        return

    city_info[town]['gold'] += gold_added
    sum_gold = city_info[town]['gold']
    print(f'{gold_added} gold added to the city treasury. {town} now has {sum_gold} gold.')

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

if len(city_info) <= 0:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')

else:
    print(f'Ahoy, Captain! There are {len(city_info)} wealthy settlements to go to:')

    for town in city_info:
        print(f"{town} -> Population: {city_info[town]['population']} citizens, Gold: {city_info[town]['gold']} kg")
