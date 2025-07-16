def ascii_sumator(start_char, end_char, random_string):
    start = ord(start_char)
    end = ord(end_char)
    lower = min(start, end)
    higher = max(start, end)
    total = 0

    for char in random_string:
        ascii_table = ord(char)
        if lower < ascii_table < higher:
            total += ascii_table
    return total

char1 = input()
char2 = input()
text = input()

print(ascii_sumator(char1, char2, text))
