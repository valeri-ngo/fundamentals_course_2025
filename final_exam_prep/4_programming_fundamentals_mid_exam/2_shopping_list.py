def urgent(item_lst: list, item: str) -> None:
    if item not in item_lst:
        item_lst.insert(0, item)

def unnecessary(item_lst: list, item: str) -> None:
    if item in item_lst:
        item_lst.remove(item)

def correct(item_lst: list, old_item: str, new_item: str) -> None:
    if old_item in item_lst:
        old_value = item_lst.index(old_item)
        item_lst[old_value] = new_item

def rearrange(item_lst: list, item) -> None:
    if item in item_lst:
        item_lst.remove(item)
        item_lst.append(item)

def main():

    item_lst = input().split('!')

    while True:

        command = input()

        if command == 'Go Shopping!':
            break

        split_into_parts = command.split()

        if split_into_parts[0] == 'Urgent':
            item = split_into_parts[1]
            urgent(item_lst, item)

        elif split_into_parts[0] == 'Unnecessary':
            item = split_into_parts[1]
            unnecessary(item_lst, item)

        elif split_into_parts[0] == 'Correct':
            old_item, new_item = split_into_parts[1], split_into_parts[2]
            correct(item_lst, old_item, new_item)

        elif split_into_parts[0] == 'Rearrange':
            item = split_into_parts[1]
            rearrange(item_lst, item)

    print(', '.join(item_lst))

if __name__ == '__main__':
    main()
