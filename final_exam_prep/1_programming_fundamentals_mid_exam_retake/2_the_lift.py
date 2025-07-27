# people_waiting = int(input())
# lift_state = list(map(int, input().split()))
#
# is_empty = False
#
# for available_space in range(len(lift_state)):
#
#     free_space = 4 - lift_state[available_space]
#     people_to_add = min(people_waiting, free_space)
#     lift_state[available_space] += people_to_add
#     people_waiting -= people_to_add
#
# if people_waiting > 0:
#     print(f"There isn't enough space! {people_waiting} people in a queue!")
#     print(' '.join(str(still_waiting) for still_waiting in lift_state))
# elif any(still_waiting < 4 for still_waiting in lift_state):
#     print(f'The lift has empty spots!')
#     print(' '.join(str(still_waiting) for still_waiting in lift_state))
# else:
#     print(' '.join(str(still_waiting) for still_waiting in lift_state))
# ---------------------------------------------------------------------------------
# people_waiting = int(input())
# lift_state = list(map(int, input().split()))
#
# index = 0
#
# while people_waiting > 0 and index < len(lift_state):
#     free_space = 4 - lift_state[index]
#
#     if free_space > 0:
#         people_to_add = min(free_space, people_waiting)
#         lift_state[index] += people_to_add
#         people_waiting -= people_to_add
#
#     index += 1
#
# if people_waiting > 0:
#     print(f"There isn't enough space! {people_waiting} people in a queue!")
# elif any(wagon < 4 for wagon in lift_state):
#     print("The lift has empty spots!")
#
# print(' '.join(str(wagon) for wagon in lift_state))

# ---------------------------------------------------------------------------------

def fill_lift(people_waiting, lift_state):
    index = 0
    while people_waiting > 0 and index < len(lift_state):
        free_space = 4 - lift_state[index]
        if free_space > 0:
            people_to_add = min(people_waiting, free_space)
            lift_state[index] += people_to_add
            people_waiting -= people_to_add
        index += 1
    return people_waiting, lift_state

def print_result(people_waiting, lift_state):
    if people_waiting > 0:
        print(f"There isn't enough space! {people_waiting} people in a queue!")
    elif any(wagon < 4 for wagon in lift_state):
        print("The lift has empty spots!")
    print(' '.join(str(wagon) for wagon in lift_state))

def list_state():
    people_waiting = int(input())
    lift_state = list(map(int, input().split()))
    people_waiting, lift_state = fill_lift(people_waiting, lift_state)
    print_result(people_waiting, lift_state)

list_state()
