first_number = int(input())
second_number = int(input())

print('Before:')
print(f'a = {first_number}')
print(f'b = {second_number}')

swappable_number = first_number
first_number = second_number
second_number = swappable_number

print('After:')
print(f'a = {first_number}')
print(f'b = {second_number}')
