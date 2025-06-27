def josephus_permutation(remove_list: list, stepped_index: int) -> list:
    removed_list = []
    index = 0

    while remove_list:
        index = (index + stepped_index -1) % len(remove_list)
        popped = remove_list.pop(index)
        removed_list.append(popped)
    return removed_list


string_input = input().split()
string_int = list(map(int, string_input))
number = int(input())

result = josephus_permutation(string_input, number)
print(f"[{','.join(map(str, result))}]")
