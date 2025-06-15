number_of_rooms = int(input())
is_room_good = True
total_chairs_available = 0

for current_room_number in range(1, number_of_rooms +1):
    current_room_info = input().split()
    current_chairs_number_as_string = current_room_info[0]
    chairs_number = len(current_chairs_number_as_string)
    current_visitors_number = int(current_room_info[1])

    if chairs_number < current_visitors_number:
        chairs_needed = current_visitors_number - chairs_number
        print(f"{chairs_needed} more chairs needed in room {current_room_number}")
        is_room_good = False
    else:
        total_chairs_available += chairs_number - current_visitors_number

if is_room_good:
    print(f"Game On, {total_chairs_available} free chairs left")