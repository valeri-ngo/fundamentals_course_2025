import re

line = input()
pattern = r'(w{3}\.[a-zA-Z0-9\-]+(\.[a-z]+)+)'
while line:
    match = re.search(pattern, line)
    if match:
        link = match.group(1)
        print(link)
    line = input()