def smallest_number(first_number: int, second_number:int, third_number:int) -> int:
    list_with_number = [first_number, second_number, third_number]
    return min(list_with_number)


first_number_ = int(input())
second_number_ = int(input())
third_number_ = int(input())

print(smallest_number(first_number_, second_number_, third_number_))
