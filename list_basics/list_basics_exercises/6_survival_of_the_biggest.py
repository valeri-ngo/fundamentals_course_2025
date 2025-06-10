numbers = input()
numbers_to_remove = int(input())
number_as_integer = [int(num) for num in numbers.split()]
lowest_integer = []

for _ in range(numbers_to_remove):
    if number_as_integer:
        lowest_integer = number_as_integer[0]
        for num in number_as_integer:
            if num < lowest_integer:
                lowest_integer = num
        number_as_integer.remove(lowest_integer)

for i, num in enumerate(number_as_integer):
    if i == len(number_as_integer) - 1:
        print(num)
    else:
        print(num, end=', ')