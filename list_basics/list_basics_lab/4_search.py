n = int(input())
magical_word = input()

strings = []

for _ in range(n):
    current_string = input()
    strings.append(current_string)

filtered_strings = []

for current_string in strings:
    if magical_word in current_string:
        filtered_strings.append(current_string)

print(strings)
print(filtered_strings)

# ----------------------------------------------------------------------------------------------------------------------
#
# n = int(input())
# magic_word = input()

# strings = [input() for _ in range (n)]

# filtered_strings = [current_string for current_string in strings if magic_word in current_string]


# print(strings)
# print(filtered_strings)