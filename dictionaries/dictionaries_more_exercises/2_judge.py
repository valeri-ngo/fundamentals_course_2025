judge = {}
contests_order = []

while True:
    line_input = input()
    if line_input == "no more time":
        break

    username, contest, points = line_input.split(" -> ")
    points = int(points)

    if contest not in contests_order:
        contests_order.append(contest)

    if username not in judge:
        judge[username] = {}
    if contest not in judge[username] or points > judge[username][contest]:
        judge[username][contest] = points

contests = {}
for username, contests_dict in judge.items():
    for contest, points in contests_dict.items():
        if contest not in contests:
            contests[contest] = {}
        contests[contest][username] = points

def sort_by_points_then_name(item):
    return (-item[1], item[0])

for contest in contests_order:
    if contest in contests:
        participants = contests[contest]
        print(f"{contest}: {len(participants)} participants")

        sorted_participants = sorted(participants.items(), key=sort_by_points_then_name)

        rank = 1
        for username, points in sorted_participants:
            print(f"{rank}. {username} <::> {points}")
            rank += 1

total_score = {}
for username in judge:
    total_score[username] = sum(judge[username].values())

def sort_total(item):
    return (-item[1], item[0])

sorted_names = sorted(total_score.items(), key=sort_total)

print("Individual standings:")
position = 1
for username, total in sorted_names:
    print(f"{position}. {username} -> {total}")
    position += 1
