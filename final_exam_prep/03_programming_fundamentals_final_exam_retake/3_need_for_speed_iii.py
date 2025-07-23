def drive(car, distance, fuel):
    if cars[car]['fuel'] < fuel:
        print('Not enough fuel to make that ride')
    else:
        cars[car]['fuel'] -= fuel
        cars[car]['kilometers'] += distance
        print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if cars[car]['kilometers'] >= 100000:
            print(f'Time to sell the {car}!')
            del cars[car]

def refuel(car, fuel):
    actual_fuel_capacity = cars[car]['fuel']
    max_capacity_of_the_tank = 75
    available_capacity = max_capacity_of_the_tank - actual_fuel_capacity
    current_fuel_added = min(fuel, available_capacity)
    cars[car]['fuel'] += current_fuel_added
    print(f'{car} refueled with {current_fuel_added} liters')

def revert(car, reverted_kilometers):
    minimum_amount_of_kilometers = 10000
    current_kilometers = cars[car]['kilometers']
    current_kilometers -= reverted_kilometers
    if current_kilometers < minimum_amount_of_kilometers:
        cars[car]['kilometers'] = minimum_amount_of_kilometers
    else:
        kilometers_decreased = cars[car]['kilometers'] - current_kilometers
        cars[car]['kilometers'] = current_kilometers
        print(f'{car} mileage decreased by {kilometers_decreased} kilometers')

number_of_cars = int(input())
cars = {}

for _ in range(number_of_cars):
    car_info = input()
    car, kilometers, fuel = car_info.split('|')
    cars[car] = {'kilometers': int(kilometers),
                 'fuel': int(fuel)
                 }

command = input()

while command != 'Stop':
    list_of_commands = command.split(' : ')
    action = list_of_commands[0]
    car = list_of_commands[1]
    if action == 'Drive':
        distance = int(list_of_commands[2])
        fuel = int(list_of_commands[3])
        drive(car, distance, fuel)
    elif action == 'Refuel':
        fuel = int(list_of_commands[2])
        refuel(car, fuel)
    elif action == 'Revert':
        reverted_kilometers = int(list_of_commands[2])
        revert(car, reverted_kilometers)

    command = input()

for car, data in cars.items():
    print(f"{car} -> Mileage: {data['kilometers']} kms, Fuel in the tank: {data['fuel']} lt.")
