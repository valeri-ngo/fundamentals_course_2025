sequence_of_elements = input().split()
move_count = 0

while True:
    command = input()

    if command == 'end':
        print("Sorry you lose :(")
        print(' '.join(sequence_of_elements))
        break

    index1, index2 = map(int, command.split())

    if (index1 == index2 or index1 < 0 or index2 < 0
            or index1 >= len(sequence_of_elements)
            or index2 >= len(sequence_of_elements)):

            move_count += 1
            middle_of_the_sequence = len(sequence_of_elements) // 2
            sequence_of_elements.insert(middle_of_the_sequence, f'-{move_count}a')
            sequence_of_elements.insert(middle_of_the_sequence, f'-{move_count}a')
            print(f'Invalid input! Adding additional elements to the board')
            continue

    if sequence_of_elements[index1] == sequence_of_elements[index2]:
        print(f'Congrats! You have found matching elements - {sequence_of_elements[index1]}!')
        move_count += 1

        first_index, second_index = sorted([index1, index2], reverse=True)
        sequence_of_elements.pop(first_index)
        sequence_of_elements.pop(second_index)

        if not sequence_of_elements:
            print(f'You have won in {move_count} turns!')
            break

    else:
        print(f'Try again!')
        move_count += 1
