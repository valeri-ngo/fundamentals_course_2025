from example import sum_numbers

for _ in range(5):
    a = int(input('Въведи стойност за "А": '))
    b = int(input('Въведи стойност за "B": '))
    c = int(input('Въведи стойност за "C": '))

    result = sum_numbers(a, b, c)      ## Аргументи
    print(result)