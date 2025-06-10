# animals = input().split(', ')
#
# animals = animals[::-1]
#
# wolf_number = animals.index('wolf')
#
# if wolf_number == 0:
#     print(f'Please go away and stop eating my sheep')
# else:
#     print(f'Oi! Sheep number {wolf_number}! You are about to be eaten by a wolf!')

animals = input().split(', ')

for current_animal in range(len(animals)-1, -1, -1):
    if animals[current_animal] == 'wolf':
        if current_animal == len(animals) -1:
            print(f'Please go away and stop eating my sheep')
        else:
            sheep_number = len(animals) -1 -current_animal
            print(f'Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!')
            break
