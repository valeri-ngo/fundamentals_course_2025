gifts = input().split()

while True:
    command = input()
    if command == 'No Money':
        break

    current_gift = command.split()
    index = current_gift[0]

    if index == 'OutOfStock':
        gift_to_replace = current_gift[1]
        gifts = ['None' if gift == gift_to_replace else gift for gift in gifts]

    elif index == 'Required':
        gift_name = current_gift[1]
        index = int(current_gift[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift_name

    elif index == 'JustInCase':
        gift_name = current_gift[1]
        gifts[-1] = gift_name

filtered_gifts = [gift for gift in gifts if gift != 'None']
print(' '.join(filtered_gifts))
