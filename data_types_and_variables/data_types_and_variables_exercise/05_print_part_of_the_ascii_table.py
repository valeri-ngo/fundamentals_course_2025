starting_char = int(input())
final_char = int(input())

for character in range(starting_char, final_char +1):
    if character == final_char:
        print(chr(character))
    else:
        print(chr(character),end =' ')