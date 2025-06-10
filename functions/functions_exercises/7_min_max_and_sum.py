def min_function(number:list) -> list:
    return min(number)

def max_function(number:list) -> list:
    return max(number)

def sum_function(number:list) -> int:
    return sum(number)


numbers_as_string = input().split()
numbers_as_digits = []
index = 0

for numbers in numbers_as_string:
    numbers_as_digits.append(int(numbers))

print(f'The minimum number is', min_function(numbers_as_digits))
print(f'The maximum number is', max_function(numbers_as_digits))
print(f'The sum number is:', sum_function(numbers_as_digits))