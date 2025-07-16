morse_code_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
                   '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
                   '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
                   '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}

morse_code_input = input()
words = morse_code_input.split(' | ')
save_morse_code = []

for code in words:
    letters = code.split()
    translated_letters = []
    for letter in letters:
        if letter in morse_code_dict:
            translated_letters.append(morse_code_dict[letter])
    save_morse_code.append(''.join(translated_letters))

print(' '.join(save_morse_code))
