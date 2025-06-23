def add_lesson(list_of_lessons: list, title: str) -> list:
    if title not in list_of_lessons:
        list_of_lessons.append(title)
    return list_of_lessons


def insert_lesson(list_of_lessons: list, title: str, current_index: int) -> list:
    if title not in list_of_lessons:
        list_of_lessons.insert(current_index, title)
    return list_of_lessons


def remove_lesson(list_of_lessons: list, title: str) -> list:
    if title in list_of_lessons:
        list_of_lessons.remove(title)
        exercise_name = f"{title}-Exercise"
        if exercise_name in list_of_lessons:
            list_of_lessons.remove(exercise_name)
    return list_of_lessons


def swap_lesson(list_of_lessons: list, first_lesson: str, second_lesson: str) -> list:
    if first_lesson in list_of_lessons and second_lesson in list_of_lessons:
        first_position = list_of_lessons.index(first_lesson)
        second_position = list_of_lessons.index(second_lesson)
        first_lesson_has_exercise = False
        second_lesson_has_exercise = False
        if first_position + 1 in range(len(list_of_lessons)):
            first_lesson_has_exercise = \
                f"{first_lesson}-Exercise" in \
                list_of_lessons[first_position + 1]
        if second_position + 1 in range(len(list_of_lessons)):
            second_lesson_has_exercise = \
                f"{second_lesson}-Exercise" in \
                list_of_lessons[second_position + 1]
        # First swap lessons
        list_of_lessons[first_position], list_of_lessons[second_position] = \
            list_of_lessons[second_position], list_of_lessons[first_position]

        # Time for swap exercise
        # Case where bot lessons has exercises
        if first_lesson_has_exercise and second_lesson_has_exercise:
            list_of_lessons[first_position + 1], list_of_lessons[second_position + 1] = \
                list_of_lessons[second_position + 1], list_of_lessons[first_position + 1]
        # Case where first has exercise, second has not exercise
        elif first_lesson_has_exercise and not second_lesson_has_exercise:
            list_of_lessons.insert(second_position + 1,
                                   list_of_lessons.pop(first_position + 1))
        # Case where second has exercise, first has not exercise
        elif not first_lesson_has_exercise and second_lesson_has_exercise:
            list_of_lessons.insert(first_position + 1,
                                   list_of_lessons.pop(second_position + 1))
    return list_of_lessons


def exercise(list_of_lessons: list, title: str) -> list:
    exercise_name = f"{title}-Exercise"
    if title in list_of_lessons and exercise_name not in list_of_lessons:
        lesson_index = list_of_lessons.index(title)
        list_of_lessons.insert(lesson_index + 1, exercise_name)
    elif title not in list_of_lessons:  # else
        list_of_lessons.append(title)
        list_of_lessons.append(exercise_name)
    return list_of_lessons


lessons = input().split(", ")
command = input().split(":")
while len(command) > 1:  # while command[0]!= "course start"
    action = command[0]
    lesson_title = command[1]
    if action == "Add":
        lessons = add_lesson(lessons, lesson_title)
    elif action == "Insert":
        index = int(command[2])
        lessons = insert_lesson(lessons, lesson_title, index)
    elif action == "Remove":
        lessons = remove_lesson(lessons, lesson_title)
    elif action == "Swap":
        new_title = command[2]
        lessons = swap_lesson(lessons, lesson_title, new_title)
    elif action == "Exercise":
        lessons = exercise(lessons, lesson_title)
    command = input().split(":")
for index, lesson_or_exercise_name in enumerate(lessons):
    print(f"{index + 1}.{lesson_or_exercise_name}")