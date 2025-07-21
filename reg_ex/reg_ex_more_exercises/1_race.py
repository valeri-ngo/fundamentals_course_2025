import re

participants = input().split(', ')
results = {}

pattern_name = r'([a-zA-Z]+)'
pattern_digits = r'([\d])'

line = input()

while line != 'end of race':
    name = ''.join(re.findall(pattern_name, line))
    distance = sum(int(x) for x in re.findall(pattern_digits, line))

    if name in participants:
        if name not in results:
            results[name] = 0
        results[name] += distance

    line = input()

sorted_results = sorted(results.items(), key=lambda x: -x[1])

places = ['1st', '2nd', '3rd']

for i in range(min(3, len(sorted_results))):
    print(f"{places[i]} place: {sorted_results[i][0]}")