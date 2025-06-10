# my_list = ['apple', 'orange', 'banana', 'kiwi', 'cherry']
#
# For loop
#
# for index in range (len(my_list)):
#     print(f'Index - {index}, Element --> {my_list[index]}')
#
# for item in my_list:
#     print(f'Element - {item}, Index --> {my_list.index(item)}')
#
# # While loop
#
# my_list = ['apple', 'orange', 'banana', 'kiwi', 'cherry']
#
# index = 0
#
# while index < len(my_list):
#     index += 1
#     print(f'Index - {index}, Element -- > {my_list[index+1]}')
#
# # Even and Odd numbers
#
# even_number = [number for number in [1,2,3,4,5,6,7,8,9,10] if number % 2 == 0]
# odd_number = [number for number in [1,2,3,4,5,6,7,8,9,10] if number % 3 == 0]
# print(even_number, odd_number)
#
# Comprehension
#
# n = int(input())
# number = [int(input()) for _ in range (n)]
# positive = [num for num in number if num >= 0]
# negative = [num for num in number if num < 0]
#
# print(positive)
# print(negative)
# print(f'Count of positives: {len(positive)}')
# print(f'Sum of negatives: {sum(negative)}')

# Find a string
#
# my_list = [1, 2, 'current_string', 4, 5]
# string_a = []
# if 'current_string' in my_list:
#     string_a.append('current_string')
#     magical_string = 'current_string'
#     print(magical_string)


# Reverse index removing
#
# my_list = [1, 2, 3, 4, 5, 'Pesho', 'Gosho', 'Atanas']
# for index in range(len(my_list) -1, -1, -1):
#     print(f'Removing {my_list.pop(index)}')

help(list)
