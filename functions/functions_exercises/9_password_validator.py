def password_validator(some_password:str) -> str:
    list_with_error_messages = []
    if len(some_password) < 6 or len(some_password) > 10:
        list_with_error_messages.append('Password must be between 6 and 10 characters')
    if not some_password.isalnum():
        list_with_error_messages.append('Password must consist only of letters and digits')
    digits_counter = 0
    for current_character in some_password:
        if current_character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        list_with_error_messages.append('Password must have at least 2 digits')
    return list_with_error_messages

password_input = input()
error_messages = password_validator(password_input)
if not error_messages:
    print('Password is valid')
else:
    print('\n'.join(error_messages))
