some_text = input()
encrypted_text = ''
for character in some_text:
    encrypted_character = chr(ord(character) + 3)
    encrypted_text += encrypted_character
print(encrypted_text)