numbers_as_string = input().split(', ')
even_numbers = [current_index for current_index, num in enumerate(numbers_as_string) if int(num) % 2 == 0]
print(even_numbers)
