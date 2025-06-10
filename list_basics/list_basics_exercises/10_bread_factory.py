events = input().split('|')

current_energy = 100
current_coins = 100
bakery_is_open = True

for event in events:
    event_items = event.split('-')
    type_of_event = event_items[0]
    value_of_event = int(event_items[1])

    if type_of_event == 'rest':
        initial_energy = current_energy
        current_energy += value_of_event

        if current_energy > 100:
            current_energy = 100
        gained_energy = current_energy - initial_energy

        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {current_energy}.')

    elif type_of_event == 'order':

        if current_energy >= 30:
            current_coins += value_of_event
            current_energy -= 30
            print(f'You earned {value_of_event} coins.')

        else:
            current_energy += 50
            print(f'You had to rest!')
    else:

        if current_coins >= value_of_event:
            current_coins -= value_of_event
            print(f'You bought {type_of_event}.')
        else:

            print(f'Closed! Cannot afford {type_of_event}.')
            bakery_is_open = False
            break

if bakery_is_open:
    print(f'Day completed!')
    print(f'Coins: {current_coins}')
    print(f'Energy: {current_energy}')