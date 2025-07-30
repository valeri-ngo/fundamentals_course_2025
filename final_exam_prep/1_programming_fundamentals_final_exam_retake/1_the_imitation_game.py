def move(message: str, number_of_letters: int) -> str:
    return message[number_of_letters:] + message[:number_of_letters]
def insert(message: str, index: int, value: str) -> str:
    return message[:index] + value + message[index:]
def change_all(message: str, substring: str, replacement: str) -> str:
    return message.replace(substring, replacement)

encrypted_message = input()
command = input()

while command != 'Decode':
    parts = command.split('|')
    action = parts[0]

    if action == 'Move':
        number_of_letters = int(parts[1])
        encrypted_message = move(encrypted_message, number_of_letters)
    elif action == 'Insert':
        index = int(parts[1])
        value = parts[2]
        encrypted_message = insert(encrypted_message, index, value)
    elif action == 'ChangeAll':
        substring = parts[1]
        replacement = parts[2]
        encrypted_message = change_all(encrypted_message, substring, replacement)

    command = input()

print(f'The decrypted message is: {encrypted_message}')