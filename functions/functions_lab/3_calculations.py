# def add(a, b):
#     return a + b
# def subtract (a, b):
#     return a - b
# def multiply(a, b):
#     return a * b
# def divide(a, b):
#     return int(a / b)
#
# def calculator():
#     operator = input()
#     number_1 = int(input())
#     number_2 = int(input())
#     sum_result = 0
#
#     if operator == 'add':
#         sum_result = add(number_1, number_2)
#     elif operator == 'subtract':
#         sum_result = subtract(number_1, number_2)
#     elif operator == 'multiply':
#         sum_result = multiply(number_1, number_2)
#     elif operator == 'divide':
#         sum_result = divide(number_1, number_2)
#     print(sum_result)
#
# calculator()


def calculate_results(operator:str, num1:int, num2:int):
    return {
        'add': num1 + num2 ,
        'subtract': num1 - num2 ,
        'multiply': num1 * num2 ,
        'divide': int(num1 / num2)
    }.get(operator)


operator_ = input()
num1_ = int(input())
num2_ = int(input())
result = calculate_results(operator_, num1_, num2_)
print(result)
