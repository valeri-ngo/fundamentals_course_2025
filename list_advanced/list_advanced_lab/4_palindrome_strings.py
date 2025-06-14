# strings = input().split()
# searched_palindrome = input()
# palindromes = []
# palindrome_counter = 0
#
# for word in strings:
#     if word == word[::-1]:
#         palindromes.append(word)
#
# for current_palindrome in palindromes:
#     if current_palindrome == searched_palindrome:
#         palindrome_counter +=1
#
# print(f'{palindromes}')
# print(f'Found palindrome {palindrome_counter} times')
# ---
#
def is_palindrome(word):
    return word == word[::-1]
def palindrome_list(word_list):
    return [word for word in word_list if is_palindrome(word)]
def count_palindromes(palindrome,counter):
    return palindrome.count(counter)

strings = input().split()
searched_word = input()

palindromes = palindrome_list(strings)
palindrome_counter = count_palindromes(palindromes,searched_word)
print(f'{palindromes}')
print(f'Found palindrome {palindrome_counter} times')