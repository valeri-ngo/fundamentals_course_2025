import re

given_text = input()

text_before_regex = r'([#@])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
text_after_regex = re.findall(text_before_regex, given_text)
mirrored_words = []
total_pairs = len(text_after_regex)

for match in text_after_regex:
    if match[1] == match[2][::-1]:
        mirrored_words.append(f'{match[1]} <=> {match[2]}')

if total_pairs > 0:
    print(f'{total_pairs} word pairs found!')
else:
    print(f'No word pairs found!')

if mirrored_words:
    print(f'The mirror words are:')
    print(f', '.join(mirrored_words))
else:
    print(f'No mirror words!')
