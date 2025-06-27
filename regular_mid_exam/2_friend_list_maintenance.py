def blacklist(name:str, blacklisted_friends:int):
    if name in friends_list:
        index = friends_list.index(name)
        friends_list[index] = "Blacklisted"
        blacklisted_friends += 1
        print(f"{name} was blacklisted.")
    else:
        print(f"{name} was not found.")
    return blacklisted_friends

def error(index:int, lost_counter:int):
    if 0 <= index < len(friends_list):
        name = friends_list[index]
        if name != "Blacklisted" and name != "Lost":
            friends_list[index] = "Lost"
            lost_counter += 1
            print(f"{name} was lost due to an error.")
    return lost_counter

def change(index:int, new_name:str):
    if 0 <= index < len(friends_list):
        current_name = friends_list[index]
        friends_list[index] = new_name
        print(f"{current_name} changed his username to {new_name}.")

def report():
    print(f"Blacklisted names: {blacklisted_friends}")
    print(f"Lost names: {lost_counter}")
    print(" ".join(friends_list))

friends_list = input().split(", ")
blacklisted_friends = 0
lost_counter = 0

while True:
    command = input().split()

    if command[0] == "Report":
        report()
        break
    elif command[0] == "Blacklist":
        name_input = command[1]
        blacklisted_friends = blacklist(name_input, blacklisted_friends)
    elif command[0] == "Error":
        index_input = int(command[1])
        lost_counter = error(index_input, lost_counter)
    elif command[0] == "Change":
        index_input = int(command[1])
        new_name = command[2]
        change(index_input, new_name)
