def check_palindromes(number_as_string:str) -> list:
    palindrome_as_string = number_as_string.split(', ')
    palindromes_list = []

    for current_string in palindrome_as_string:
        if current_string == current_string[::-1]:
            palindromes_list.append(True)
        else:
            palindromes_list.append(False)

    return palindromes_list

palindrome_input = input()
result = check_palindromes(palindrome_input)
for res in result:
    print(res)