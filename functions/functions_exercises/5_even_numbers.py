def even(number:int) -> bool:
    return number % 2 == 0

numbers_as_string = input().split()
numbers_as_digits = []
for current_number in numbers_as_string:
    numbers_as_digits.append(int(current_number))
final_result = list(filter(even, numbers_as_digits))
print(final_result)
