def take_odd(new_password: str):
    new_password = ''.join([new_password[index] for index in range(len(new_password)) if index % 2 != 0])
    print(new_password)
    return new_password

def cut(new_string: str, index: int, length: int):
    substring = new_string[index:index+length]
    new_string = new_string.replace(substring, '', 1)
    print(new_string)
    return new_string

def substitute_(new_string: str, substring: str, substitute: str):

    if substring in new_string:
        new_string = new_string.replace(substring, substitute)
        print(new_string)

    else:
        print('Nothing to replace!')

    return new_string

def main():

    new_string = input()

    while True:

        command = input()

        if command == 'Done':
            break

        parts = command.split()
        action = parts[0]

        if action == 'TakeOdd':
            new_string = take_odd(new_string)

        elif action == 'Cut':
            index, length = int(parts[1]), int(parts[2])
            new_string = cut(new_string, index, length)

        elif action == 'Substitute':
            substring, substitute = parts[1], parts[2]
            new_string = substitute_(new_string, substring, substitute)

    print(f"Your password is: {new_string}")

if __name__ == '__main__':
    main()