def merge(data_input, start, end):
    elements_to_merge = data_input[start:end +1]
    merged = "".join(elements_to_merge)

    for _ in range(end - start + 1):
        data_input.pop(start)
    data_input.insert(start, merged)


def divide(data_input, index, partitions):
    element = data_input[index]
    part_length = len(element) // partitions
    remainder = len(element) % partitions

    parts = []

    current_position = 0

    for i in range(partitions):
        current_part_length = part_length

        if i == partitions -1:
            current_part_length += remainder

        part = element[current_position:current_position + current_part_length]
        parts.append(part)

        current_position += current_part_length

    data_input.pop(index)

    for i,part in enumerate(parts):
        data_input.insert(index + i, part)

string_input = input().split()

while True:
    command = input().split()
    if command[0] == "3:1":
        break

    elif command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index >= len(string_input):
            end_index = len(string_input ) -1
        merge(string_input, start_index, end_index)

    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])
        divide(string_input, index, partitions)

print(" ".join(string_input))