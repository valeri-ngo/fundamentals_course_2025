import re

all_matches = []
line = input()

while line:
    pattern = r"\d+"
    matches = re.findall(pattern, line)
    if matches:
        all_matches += matches
    line = input()
print(' '.join(all_matches))