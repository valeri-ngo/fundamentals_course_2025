courses = {}

while True:
    course_title = input()
    if course_title == "end":
        break

    course_name, student_name = course_title.split(" : ")
    if course_name not in courses.keys():
        courses[course_name] = []
    courses[course_name].append(student_name)

for course_name, student_list in courses.items():
    print(f"{course_name}: {len(student_list)}")
    for student_name in student_list:
        print(f"-- {student_name}")
