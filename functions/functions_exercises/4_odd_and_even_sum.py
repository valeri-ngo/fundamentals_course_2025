def odd_even_sum(some_text:str) -> str:
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in some_text:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)
    return f'Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}'



digits = input()
print(odd_even_sum(digits))