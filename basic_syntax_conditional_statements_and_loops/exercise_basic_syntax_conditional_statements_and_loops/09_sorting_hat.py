command = input()
name_len = 0

while command != 'Welcome!' and command != 'Voldemort':

    name_len = len(command)

    if 0 < name_len < 5:
        print(f"{command} goes to Gryffindor.")

    elif name_len == 5:
        print(f"{command} goes to Slytherin.")

    elif name_len == 6:
        print(f"{command} goes to Ravenclaw.")

    elif name_len > 6:
        print(f"{command} goes to Hufflepuff.")

    command = input()

if command == 'Voldemort':
    print(f'You must not speak of that name!')

elif command == 'Welcome!':
    print(f'Welcome to Hogwarts.')
