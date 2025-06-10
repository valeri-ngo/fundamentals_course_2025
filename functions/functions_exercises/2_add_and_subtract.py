def sum_numbers(first:int, second:int) -> int:
    return first + second
def subtract(result:int, third:int) -> int:
    return result - third
def add_and_subtract(first:int, second:int, third:int):
    sum_of_numbers = sum_numbers(first, second)
    final_result = subtract(sum_of_numbers, third)
    return final_result

first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))