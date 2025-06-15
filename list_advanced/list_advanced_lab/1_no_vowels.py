text = input()
vowels_list = [ch for ch in text if ch.lower() not in ['a', 'o', 'u', 'e', 'i']]
print(''.join(vowels_list))
