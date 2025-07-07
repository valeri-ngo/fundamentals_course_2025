unique_force_user = {}

while True:
    side_input = input()
    if side_input == "Lumpawaroo":
        break

    if " | " in side_input:
        side, user = side_input.split(" | ")
        user_exists = False
        for users in unique_force_user.values():
            if user in users:
                user_exists = True
                break
        if not user_exists:
            if side not in unique_force_user:
                unique_force_user[side] = []
            unique_force_user[side].append(user)
    elif " -> " in side_input:
        user, side = side_input.split(" -> ")
        user_exists = False
        for current_side, users in unique_force_user.items():
            if user in users:
                user_exists = True
                old_side = current_side
                break
        if user_exists:
            unique_force_user[old_side].remove(user)

        if side not in unique_force_user:
            unique_force_user[side] = []
        unique_force_user[side].append(user)
        print(f"{user} joins the {side} side!")
for side, users in unique_force_user.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
