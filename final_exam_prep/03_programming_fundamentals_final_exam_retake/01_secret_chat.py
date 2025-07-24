def insert_space(message: str, index: int) -> str:
    return message[:index] + ' ' + message[index:]

def reverse(message: str, substring: str) -> str:
    if substring in message:
        message = message.replace(substring, '', 1)
        reversed_string = substring[::-1]
        message += reversed_string
        return message
    else:
        return 'error'

def change_all(message: str, substring: str, replaced_string: str) -> str:
    return message.replace(substring, replaced_string)

message = input()

is_reveal = False

while not is_reveal:
    command = input()
    if command == 'Reveal':
        print(f'You have a new text message: {message}')
        is_reveal = True
    else:
        split_action = command.split(':|:')

        if split_action[0] == 'InsertSpace':
            inserted_space = int(split_action[1])
            message = insert_space(message, inserted_space)
            print(message)

        elif split_action[0] == 'Reverse':
            substring = split_action[1]
            result = reverse(message, substring)
            if result != 'error':
                message = result
                print(message)
            else:
                print('error')

        elif split_action[0] == 'ChangeAll':
            substring_changed = split_action[1]
            replaced_string = split_action[2]
            message = change_all(message, substring_changed, replaced_string)
            print(message)