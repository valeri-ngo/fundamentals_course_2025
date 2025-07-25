def rate(plant_dict: dict, plant: str, rating: int) -> None:
    plant_dict[plant]['rating'].append(rating)
def update(plant_dict: dict, plant: str, new_rarity: int) -> None:
    plant_dict[plant]['rarity'] = new_rarity
def reset(plant_dict: dict, plant: str) -> None:
    plant_dict[plant]['rating'].clear()

cycle_number = int(input())

plant_dict = {}

for _ in range(cycle_number):
    current_plant = input()
    plant, rarity = current_plant.split('<->')
    plant_dict[plant] = {'rarity': int(rarity),
                         'rating': []}

while True:
    current_command = input()

    if current_command == 'Exhibition':
        break
    command_split = current_command.split(': ')
    actual_action = command_split[0]
    actual_parameters = command_split[1]

    if actual_action == 'Rate':
        plant, rating = actual_parameters.split(' - ')
        if plant in plant_dict:
            rate(plant_dict, plant, int(rating))
        else:
            print('error')

    elif actual_action == 'Update':
        plant, new_rarity = actual_parameters.split(' - ')
        if plant in plant_dict:
            update(plant_dict, plant, int(new_rarity))
        else:
            print('error')

    elif actual_action == 'Reset':
        plant = actual_parameters
        if plant in plant_dict:
            reset(plant_dict, plant)
        else:
            print('error')
print('Plants for the exhibition:')

for plant, data in plant_dict.items():
    average_rating = sum(data['rating']) / len(data['rating']) if data['rating'] else 0
    print(f"- {plant}; Rarity: {data['rarity']}; Rating: {average_rating:.2f}")