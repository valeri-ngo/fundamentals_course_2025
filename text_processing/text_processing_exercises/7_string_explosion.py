text_string = input()
final_string = ''
strength = 0

for index in range(len(text_string)):
    # Explosion
    if strength > 0 and text_string[index] != '>':
        strength -= 1
    # Explosion mark
    elif text_string[index] == '>':
        final_string += '>'
        strength += int(text_string[index + 1])
    # No explosion, no explosion mark
    else:
        final_string += text_string[index]

print(final_string)
