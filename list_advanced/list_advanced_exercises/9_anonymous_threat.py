string_input = input().split()
command = input()

while command != "3:1":
    strings = command.split()
    action = strings[0]

    if action == "merge":
        starting_index = int(strings[1])
        final_index = int(strings[2])
        starting_index = max(0, starting_index)
        final_index = min(len(string_input) -1, final_index)

        if starting_index <= final_index:
            merge = ''.join(string_input[starting_index:final_index + 1])
            string_input[starting_index:final_index +1 ] = [merge]

    elif action == "divide":
        index = int(strings[1])
        partitions = int(strings[2])

        if 0 <= index < len(string_input) and partitions > 0:
            divided_string = string_input[index]
            partition_size = len(divided_string) // partitions
            extra = len(divided_string) % partitions

            new_strings = []
            starting_point = 0
            for num in range(partitions):
                added = 1 if num < extra else 0
                new_strings.append(divided_string[starting_point:starting_point + partition_size + added])
                starting_point += partition_size + added

            string_input[index:index +1] = new_strings

    command = input()

print(' '.join(string_input))