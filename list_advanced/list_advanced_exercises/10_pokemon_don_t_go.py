def sequence_of_integers(string_of_integers: list) -> list:
    return [int(num) for num in string_of_integers]

sum_removed = 0

string_as_integer = input().split(" ")
string_as_list = sequence_of_integers(string_as_integer)
while (len(string_as_list)) > 0:
    number_integers = input()
    numbers = int(number_integers)

    if numbers < 0:
        removed_index = string_as_list[0]
        string_as_list.pop(0)
        sum_removed += removed_index
        string_as_list.insert(0 , string_as_list[-1])

    elif numbers >= (len(string_as_list)):
            removed_index = string_as_list[-1]
            string_as_list.pop(-1)
            sum_removed += removed_index
            string_as_list.append(string_as_list[0])
    else:
        removed_index = string_as_list[numbers]
        string_as_list.pop(numbers)
        sum_removed += removed_index

    for current_index in range(len(string_as_list)):

        if string_as_list[current_index] <= removed_index:
            string_as_list[current_index] += removed_index
        else:
            string_as_list[current_index] -= removed_index

print(sum_removed)