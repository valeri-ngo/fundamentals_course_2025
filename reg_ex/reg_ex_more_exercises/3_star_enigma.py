import re

number_of_messages = int(input())
pattern = r'[starSTAR]'
decrypted_message = ''
targeted_planets = r'@([A-Za-z]+)[^\@\-\!\:\>]*:([\d]+)[^\@\-\!\:\>]*!(A|D)![^\@\-\!\:\>]*->([\d]+)[^\@\-\!\:\>]*'
attacked_planets = []
destroyed_planets = []

for _ in range(number_of_messages):
    encrypted_message = input()
    match = re.findall(pattern, encrypted_message, re.I)
    sum_letters = len(match)
    decrypted_message = ''

    for ch in encrypted_message:
        decrypted_message += chr(ord(ch) - sum_letters)

    planets = re.search(targeted_planets, decrypted_message)
    if planets:
        if planets.group(3) == 'A':
            attacked_planets.append(planets.group(1))

        elif planets.group(3) == 'D':
            destroyed_planets.append(planets.group(1))

print(f'Attacked planets: {len(attacked_planets)}')
for planet in sorted(attacked_planets):
    print(f'-> {planet}')
print(f'Destroyed planets: {len(destroyed_planets)}')
for planet in sorted(destroyed_planets):
    print(f'-> {planet}')
