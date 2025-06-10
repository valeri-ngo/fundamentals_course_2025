n = int(input())

phrase_is_not_pure = False

for _ in range(n):
    phrase = input()

    for char in phrase:

        if char == "," or char == "." or char == "_":
            phrase_is_not_pure = True
            print(f"{phrase} is not pure!")
            break
    else:
        print(f'{phrase} is pure.')
