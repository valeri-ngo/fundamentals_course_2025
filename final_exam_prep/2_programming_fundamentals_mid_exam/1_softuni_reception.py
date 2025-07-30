number_of_students = 0
current_hour = 0

for _ in range(3):
    help_per_employee = int(input())
    number_of_students += help_per_employee

students_count = int(input())

while students_count > 0:
    current_hour += 1
    if current_hour % 4 == 0:
        continue
    else:
        students_count -= number_of_students

print(f'Time needed: {current_hour}h.')