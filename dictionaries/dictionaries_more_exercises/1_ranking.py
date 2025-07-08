ranking = {}
submissions = {}

while True:
    line_input = input()

    if line_input == 'end of contests':
        break

    contest, password = line_input.split(":")
    ranking[contest] = password

while True:
    current_contest = input()
    if current_contest == "end of submissions":
        break

    contest, current_password, username, points = current_contest.split("=>")
    points = int(points)

    if contest in ranking and ranking[contest] == current_password:
        if username not in submissions:
            submissions[username] = {}
        if contest not in submissions[username]:
            submissions[username][contest] = points
        else:
            if points > submissions[username][contest]:
                submissions[username][contest] = points

best_student = ""
highest_grade = 0

for user in submissions:
    current_grade = 0
    for contest in submissions[user]:
        current_grade += submissions[user][contest]

    if current_grade > highest_grade:
        highest_grade = current_grade
        best_student = user

print(f"Best candidate is {best_student} with total {highest_grade} points.")
print("Ranking:")

sorted_users = sorted(submissions.keys())

for user in sorted_users:
    print(user)

    sorted_contests = sorted(submissions[user].items())

    for i in range(len(sorted_contests)):
        for j in range(i + 1, len(sorted_contests)):
            if sorted_contests[i][1] < sorted_contests[j][1]:
                sorted_contests[i], sorted_contests[j] = sorted_contests[j], sorted_contests[i]

    for contest, points in sorted_contests:
        print(f"#  {contest} -> {points}")