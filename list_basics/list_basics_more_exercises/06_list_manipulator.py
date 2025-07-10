list_of_integers = list(map(int, input().split()))
while True:
    command = input()

    if command == 'end':
        break

    command_split = command.split()

    if command_split[0] == 'exchange':
        index = int(command_split[1])
        if index < 0 or index >= len(list_of_integers):
            print('Invalid index')
        else:
            list_of_integers = list_of_integers[index + 1:] + list_of_integers[:index + 1]
    elif command_split[0] in ('max', 'min'):
        pair = command_split[1]
        if pair == 'even':
            filtered_numbers = [num for num in list_of_integers if num % 2 == 0]
        else:
            filtered_numbers = [num for num in list_of_integers if num % 2 != 0]
        if not filtered_numbers:
            print('No matches')
        else:
            if command_split[0] == 'max':
                sum_numbers = max(filtered_numbers)
            else:
                sum_numbers = min(filtered_numbers)

            for numbers in range(len(list_of_integers) -1, -1, -1):
                if list_of_integers[numbers] == sum_numbers:
                    print(numbers)
                    break

    elif command_split[0] in ('first', 'last'):
        count = int(command_split[1])
        pair = command_split[2]
        if count > len(list_of_integers):
            print('Invalid count')
            continue
        if pair == 'even':
            filter_num = [num for num in list_of_integers if num % 2 == 0]
        else:
            filter_num = [num for num in list_of_integers if num % 2 != 0]

        if command_split[0] == 'first':
            print(filter_num[:count])
        else:
            print(filter_num[-count:] if count > 0 else [])

print(list_of_integers)