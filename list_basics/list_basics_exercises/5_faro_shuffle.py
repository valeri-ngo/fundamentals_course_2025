string = input().split()        ## String input
number_of_shuffles = int(input())       ## How many times it will shuffle the deck

for shuffle in range(number_of_shuffles):
    middle_side = len(string) // 2
    left_side = []
    right_side = []

    for current_left_side in range(middle_side):
        left_side.append(string[current_left_side])

    for current_right_side in range(middle_side, len(string)):
        right_side.append(string[current_right_side])

    start_shuffle = []

    for shuffled in range(middle_side):
        start_shuffle.append(left_side[shuffled])
        start_shuffle.append(right_side[shuffled])

    string = start_shuffle

print(string)