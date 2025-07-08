moba_challenger = {}

while True:
    line = input()
    if line == "Season end":
        break
    if " -> " in line:
        player, position, skill = line.split(" -> ")
        skill = int(skill)

        if player not in moba_challenger:
            moba_challenger[player] = {}
        if position not in moba_challenger[player]:
            moba_challenger[player][position] = skill
        else:
            if skill > moba_challenger[player][position]:
                moba_challenger[player][position] = skill

    elif " vs " in line:
        player1, player2 = line.split(" vs ")
        if player1 in moba_challenger and player2 in moba_challenger:
            positions_for_player1 = set(moba_challenger[player1].keys())
            positions_for_player2 = set(moba_challenger[player2].keys())

            if positions_for_player1 & positions_for_player2:
                total1 = sum(moba_challenger[player1].values())
                total2 = sum(moba_challenger[player2].values())

                if total1 > total2:
                    del moba_challenger[player2]
                elif total2 > total1:
                    del moba_challenger[player1]

sorted_player = sorted(moba_challenger.items(), key=lambda x: (-sum(x[1].values()), x[0]))
for player, positions in sorted_player:
    total_skill = sum(positions.values())
    print(f"{player}: {total_skill} skill")
    for pos, skill in sorted(positions.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {pos} <::> {skill}")