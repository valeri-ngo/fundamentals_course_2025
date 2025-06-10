word = input()
upper_letter = []

for i,letter in enumerate(word):

    if letter.isupper():
        upper_letter.append(i)

print(upper_letter)