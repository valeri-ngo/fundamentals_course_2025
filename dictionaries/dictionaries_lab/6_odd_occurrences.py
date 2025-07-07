words = input().split()

word_counts = {}

for word in words:
    lower_word = word.lower()
    if lower_word not in word_counts:
        word_counts[lower_word] = 0
    word_counts[lower_word] += 1

for(key, value) in word_counts.items():
    if value % 2 != 0:
        print(key, end=" ")