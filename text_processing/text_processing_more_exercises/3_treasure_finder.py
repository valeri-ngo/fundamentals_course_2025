key_value = list(map(int, input().split()))

while True:
    encrypted_msg = input()
    if encrypted_msg == 'find':
        break

    decrypted = ''
    ascii_index = 0

    for i in range(len(encrypted_msg)):
        key = key_value[ascii_index]
        decrypted += chr(ord(encrypted_msg[i]) - key)

        ascii_index += 1
        if ascii_index == len(key_value):
            ascii_index = 0
    start_type = decrypted.find('&') + 1
    end_type = decrypted.find('&', start_type)
    treasure_type = decrypted[start_type:end_type]

    start_cords = decrypted.find('<') + 1
    end_cords = decrypted.find('>', start_cords)
    final_cords = decrypted[start_cords:end_cords]

    print(f"Found {treasure_type} at {final_cords}")
