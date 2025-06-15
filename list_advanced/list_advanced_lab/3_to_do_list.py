def processes_todo():
    todo_notes = []

    while True:
        note = input()

        if note == 'End':
            break

        priority,task = note.split('-')
        todo_notes.append((int(priority),task))

    sorted_notes = sorted(todo_notes)
    return [task for _, task in sorted_notes]

result = processes_todo()
print(result)
