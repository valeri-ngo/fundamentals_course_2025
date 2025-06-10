string_input = input()
magical_words = ['sand', 'water', 'fish', 'sun']
word_count = 0

string_to_lower_case = string_input.lower()

for word in magical_words:
    word_count += string_to_lower_case.count(word)
print(word_count)