planned_stops = input()
command = input()
while command != 'Travel':
    list_commands = command.split(":")
    if list_commands[0] == 'Add Stop':
        index, insert = int(list_commands[1]), list_commands[2]
        if 0 <= index <= len(planned_stops):
            planned_stops = planned_stops[:index] + insert + planned_stops[index:]
        print(planned_stops)

    elif list_commands[0] == 'Remove Stop':
        start_index, end_index = int(list_commands[1]), int(list_commands[2])
        if 0 <= start_index <= end_index < len(planned_stops):
            planned_stops = planned_stops[:start_index] + planned_stops[end_index + 1:]
        print(planned_stops)
    elif list_commands[0] == 'Switch':
        old_string, new_string = list_commands[1], list_commands[2]
        if old_string in planned_stops:
            planned_stops = planned_stops.replace(old_string, new_string)
        print(planned_stops)

    command = input()
print(f'Ready for world tour! Planned stops: {planned_stops}')

