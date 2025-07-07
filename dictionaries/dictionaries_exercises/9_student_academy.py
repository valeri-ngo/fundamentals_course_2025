student_academy = {}
pair_of_rows = int(input())

for student in range(pair_of_rows):
    student_name = input()
    grade = float(input())

    if student_name not in student_academy.keys():
        student_academy[student_name] = []
    student_academy[student_name].append(grade)

for student_name, grades in student_academy.items():
    average_grade = sum(grades) / len(grades)

    if average_grade >= 4.5:
        print(f"{student_name} -> {average_grade:.2f}")