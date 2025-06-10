def factorial(number:int) -> int:
    result = 1

    for current_number in range(2, number +1):
        result *= current_number
    return result

def factorial_new_value(first_number:int, second_number:int) -> int:
    number_one = factorial(first_number)
    number_two = factorial(second_number)
    division_sum = number_one / number_two
    print(f'{division_sum:.2f}')

first_number = int(input())
second_number = int(input())
factorial_new_value(first_number, second_number)