def jump(neighborhood: list, position: int, hearts: int):
    position += hearts

    if position >= len(neighborhood):
        position = 0

    if neighborhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")

    else:
        neighborhood[position] -= 2

        if neighborhood[position] == 0:
            print(f"Place {position} has Valentine's day.")

    return position

def main():

    cupids_position = 0

    neighborhood_str = list(map(int, input().split('@')))

    while True:

        command = input()

        if command == 'Love!':
            break

        parts = command.split()
        action = parts[0]
        hearts = int(parts[1])

        cupids_position = jump(neighborhood_str, cupids_position, hearts)

    print(f"Cupid's last position was {cupids_position}.")
    failed_places = [house for house in neighborhood_str if house > 0]

    if not failed_places:
        print(f"Mission was successful.")

    else:
        print(f"Cupid has failed {len(failed_places)} places.")


if __name__ == '__main__':
    main()