import re

user_input = input()
pattern = r"\s((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
matches = re.findall(pattern, user_input)

for email in matches:
    print(email[0])