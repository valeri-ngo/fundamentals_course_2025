def swap(array_lst: list, index_1: int, index_2: int) -> None:
    array_lst[index_1], array_lst[index_2] = array_lst[index_2], array_lst[index_1]

def multiply(array_lst: list, index_1: int, index_2: int) -> None:
    array_lst[index_1] *= array_lst[index_2]

def decrease(array_lst: list) -> None:
    for i in range(len(array_lst)):
        array_lst[i] -= 1

array_values = input().split()
array_lst = [int(num) for num in array_values]

while True:
    command = input().split()

    if command[0] == 'end':
        break

    if command[0] == 'swap':
        swap(array_lst, int(command[1]), int(command[2]))

    elif command[0] == 'multiply':
        multiply(array_lst, int(command[1]), int(command[2]))

    elif command[0] == 'decrease':
        decrease(array_lst)

print(f', '.join(str(x) for x in array_lst))