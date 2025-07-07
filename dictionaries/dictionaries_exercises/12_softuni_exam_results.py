exam_results = {}
language_submissions = {}

while True:
    command = input()

    if command == "exam finished":
        break

    if '-banned' in command:
        username = command.split("-")[0]
        if username in exam_results:
            del exam_results[username]
        continue

    username, language, points = command.split("-")
    points = int(points)

    if username not in exam_results:
        exam_results[username] = {}

    if language not in language_submissions:
        language_submissions[language] = 0
    language_submissions[language] += 1

    if language not in exam_results[username]:
        exam_results[username][language] = points
    else:
        if points > exam_results[username][language]:
            exam_results[username][language] = points

print("Results:")
for user, pts in exam_results.items():
    sum_points = max(pts.values())
    print(f"{user} | {sum_points}")
print("Submissions:")
for langs, submissions in language_submissions.items():
    print(f"{langs} - {submissions}")
