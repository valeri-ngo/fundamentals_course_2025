# sequence_of_integers = list(map(int, input().split()))
# shots_counter = 0
#
# while True:
#
#     indices = input()
#
#     if indices == 'End':
#         break
#
#     shots = int(indices)
#
#     if 0 <= shots < len(sequence_of_integers):
#         shot_taken = sequence_of_integers[shots]
#
#         if shot_taken == -1:
#             continue
#
#         sequence_of_integers[shots] = -1
#         shots_counter += 1
#
#         for shot in range(len(sequence_of_integers)):
#             if sequence_of_integers[shot] == -1:
#                 continue
#             if sequence_of_integers[shot] > shot_taken:
#                 sequence_of_integers[shot] -= shot_taken
#             else:
#                 sequence_of_integers[shot] += shot_taken
# print(f"Shot targets: {shots_counter} -> {' '.join(map(str, sequence_of_integers))}")
# -----------------------------------------------------------------------------------------------
def shoot_target(targets: list[int], index: int) -> bool:
    if targets[index] == -1:
        return False

    shot_value = targets[index]
    targets[index] = -1

    for i in range(len(targets)):

        if targets[i] == -1:
            continue

        if targets[i] > shot_value:
            targets[i] -= shot_value

        else:
            targets[i] += shot_value

    return True

def print_result(targets: list[int], shot_count: int) -> None:

    print(f"Shot targets: {shot_count} -> {' '.join(map(str, targets))}")

def main():
    targets = list(map(int, input().split()))
    shot_count = 0

    while True:
        command = input()
        if command == 'End':
            break

        index = int(command)
        if 0 <= index < len(targets):
            if shoot_target(targets, index):
                shot_count += 1

    print_result(targets, shot_count)

if __name__ == "__main__":
    main()