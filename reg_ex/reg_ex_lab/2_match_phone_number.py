import re

phone_number = input()

regex = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"

matches = re.findall(regex, phone_number)

for i in range(len(matches)):
    if i < len(matches) -1:
        print(matches[i], end=', ')
    else:
        print(matches[i])