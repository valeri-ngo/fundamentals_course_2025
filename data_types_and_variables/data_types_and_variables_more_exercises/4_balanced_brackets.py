number = int(input())

balanced = True
opening_bracket = False

for _ in range(number):
    string = input()

    if string == '(':
        if opening_bracket:
            opening_bracket = True
            break
        opening_bracket = True
    elif string == ')':
        if not opening_bracket:
            balanced = False
            break
        opening_bracket = False
    else:
        continue

if opening_bracket:
    balanced = False

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')