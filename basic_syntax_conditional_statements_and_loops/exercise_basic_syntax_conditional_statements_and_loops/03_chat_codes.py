n = int(input())
message = ''

for _ in range (n):

    number = int(input())

    if number == 88:
        message = 'Hello'

    elif number == 86:
        message = 'How are you?'

    elif number < 88:
        message = 'GREAT!'

    else:
        message = 'Bye.'

    print(message)