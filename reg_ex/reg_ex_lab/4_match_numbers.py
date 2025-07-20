import re

data_input = input()

regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

matches = re.finditer(regex, data_input)

for match in matches:
    print(match.group(), end=' ')