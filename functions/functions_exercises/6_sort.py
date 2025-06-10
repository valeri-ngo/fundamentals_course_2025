def sorted_numbers(number:list) -> list:
    return sorted(number)


numbers_as_string = input().split()
numbers_as_digits = []

for current_number in numbers_as_string:
    numbers_as_digits.append(int(current_number))
final_result = sorted_numbers(numbers_as_digits)
print(final_result)