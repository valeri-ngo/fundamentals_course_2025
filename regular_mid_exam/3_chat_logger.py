def chat(msg:str) -> None:
    chat_list.append(msg)

def delete(msg:str) -> None:
    if msg in chat_list:
        chat_list.remove(msg)

def edit(current_message:str, new_message:str) -> None:
    if current_message in chat_list:
        index = chat_list.index(current_message)
        chat_list[index] = new_message

def pin(msg:str) -> None:
    if msg in chat_list:
        chat_list.remove(msg)
        chat_list.append(msg)

def spam(msg:list) -> None:
    chat_list.extend(msg)

def end():
    for msg in chat_list:
        print(msg)

chat_list = []


while True:
    command = input()

    command_into_parts = command.split()

    if command_into_parts[0] == "Chat":
        msg = " ".join([command_into_parts[i] for i in range (1, len(command_into_parts))])
        chat(msg)
    elif command_into_parts[0] == "Delete":
        msg = " ".join([command_into_parts[i] for i in range(1, len(command_into_parts))])
        delete(msg)
    elif command_into_parts[0] == "Edit":
        current_message = command_into_parts[1]
        new_message = " ".join([command_into_parts[i] for i in range(2, len(command_into_parts))])
        edit(current_message, new_message)
    elif command_into_parts[0] == "Pin":
        msg = " ".join([command_into_parts[i] for i in range (1,len(command_into_parts))])
        pin(msg)
    elif command_into_parts[0] == "Spam":
        msg = [command_into_parts[i] for i in range (1, len(command_into_parts))]
        spam(msg)
    elif command_into_parts[0] == "end":
        end()
        break
