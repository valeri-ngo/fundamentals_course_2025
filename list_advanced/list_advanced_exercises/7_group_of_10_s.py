def sorted_numbers(number:list) -> list:
    return sorted(number)

numbers_as_string = input().split(", ")
numbers_as_digits = [int(numbers) for numbers in numbers_as_string]

group_of_10_s = 10

while numbers_as_digits:
    current_group = [num for num in numbers_as_digits if num <= group_of_10_s]
    print(f"Group of {group_of_10_s}'s: {current_group}")

    numbers_as_digits = [num for num in numbers_as_digits if num > group_of_10_s]
    group_of_10_s += 10