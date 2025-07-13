# while True:
#     word = input()
#
#     if word == 'end':
#         break
#     else:
#         print(f"{word} = {word[::-1]}")
while (word := input()) != 'end':
    print(f"{word} = {word[::-1]}")