number = int(input())

for _ in range (number):

    word = input()

    if ',' in word or \
            '.' in word or \
            '_' in word:
        print(f'{word} is not pure!')

    else:
        print(f'{word} is pure.')
