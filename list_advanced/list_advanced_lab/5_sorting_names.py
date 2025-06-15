names_as_strings = input().split(', ')

sorted_list = sorted(names_as_strings, key=lambda x: (-len(x), x))

print(sorted_list)

# -----
#
# def sorted_names_by_length(names_as_string):
#     return sorted(names_as_string, key=lambda x: (-len(x), x))
#
# names_as_strings = input().split(', ')
# sorted_list = sorted_names_by_length(names_as_strings)
# print(sorted_list)
