key = int(input())
number = int(input())
current = ''

for current_letter in range(number):
    letter = input()
    current = (ord(letter) + key)
    word = chr(current)
    print(word, end='')
