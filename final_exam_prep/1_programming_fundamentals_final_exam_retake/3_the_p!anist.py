def add(piece: str, composer: str, key: str, dict_piece: dict) -> None:

    if piece in dict_piece:
        print(f'{piece} is already in the collection!')
    else:
        dict_piece[piece] = {'composer' : composer, 'key': key}
        print(f'{piece} by {composer} in {key} added to the collection!')

def remove(piece: str, dict_piece: dict) -> None:

    if piece in dict_piece:
        print(f'Successfully removed {piece}!')
        del dict_piece[piece]
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')

def changekey(piece: str, new_key: str, dict_piece: dict) -> None:

    if piece in dict_piece:
        print(f'Changed the key of {piece} to {new_key}!')
        dict_piece[piece]['key'] = new_key
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')

number_of_pieces = int(input())
is_stop = False
dict_piece = {}

for _ in range(number_of_pieces):
    pieces = input()
    piece, composer, key = pieces.split('|')
    dict_piece[piece] = {'composer': composer,
                            'key': key}

while not is_stop:
    command = input()

    if command == 'Stop':
        is_stop = True
        break

    action = command.split('|')

    if action[0] == 'Add':
        piece, composer, key = action[1], action[2], action[3]
        add(piece, composer, key, dict_piece)

    elif action[0] == 'Remove':
        piece = action[1]
        remove(piece, dict_piece)
    elif action[0] == 'ChangeKey':
        piece, new_key = action[1], action[2]
        changekey(piece, new_key, dict_piece)

for piece, data in dict_piece.items():
    print(f"{piece} -> Composer: {data['composer']}, Key: {data['key']}")