word = input()
coffee_needed = 0

while word != 'END':

    if word == 'dog' or\
            word == 'cat' or\
            word == 'coding' or\
            word == 'movie':
        coffee_needed += 1
    elif word == 'DOG' or\
            word == 'CAT' or\
            word == 'CODING' or\
            word == 'MOVIE':
        coffee_needed += 2

    word = input()

if coffee_needed > 5:
    print(f'You need extra sleep')
else:
    print(coffee_needed)
