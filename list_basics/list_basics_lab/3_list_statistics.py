# number = int(input())
#
# current_number = [int(input()) for _ in range (number)]
#
# positive = [num for num in current_number if num >= 0]
# negative = [num for num in current_number if num < 0]
#
# print(positive)
# print(negative)
# print(f'Count of positives: {len(positive)}')
# print(f'Sum of negatives: {sum(negative)}')
from operator import index

number = int(input())

sum_negative = []
count_positives = []

for _ in range (number):
    numbers = int(input())
    if numbers < 0:
        sum_negative.append(numbers)
    else:
        count_positives.append(numbers)

print(count_positives)
print(sum_negative)
print(f'Count of positives: {len(count_positives)}')
print(f'Sum of negatives: {sum(sum_negative)}')

