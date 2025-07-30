sequence_of_integers = input()
list_as_integers = list(map(int, sequence_of_integers.split()))

average_number = sum(list_as_integers) / len(list_as_integers)
numbers_above_average = []

for number in list_as_integers:
    if number > average_number:
        numbers_above_average.append(number)

if numbers_above_average:
    numbers_sorted = sorted(numbers_above_average, reverse=True)
    print(*numbers_sorted[:5])
else:
    print('No')
