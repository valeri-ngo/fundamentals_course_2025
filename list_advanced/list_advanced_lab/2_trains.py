wagon_list = [0] * int(input())

while True:
    command = input().split()

    current_command = command[0]
    if current_command == 'End':
        print(wagon_list)
        break
    elif current_command == 'add':
        number_of_people = int(command[1])
        wagon_list[-1] += number_of_people
    elif current_command == 'insert':
        index = int(command[1])
        people = int(command[2])
        wagon_list[index] += people
    elif current_command == 'leave':
        index = int(command[1])
        people = int(command[2])
        wagon_list[index] -= people
