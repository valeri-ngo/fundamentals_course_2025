# current_year = int(input())
#
# while True:
#     current_year += 1
#     current_years_as_str = str(current_year)
#     if (len(set(current_years_as_str))) == \
#         len(current_years_as_str):
#         break
#
# print(current_year)

current_year = int(input())

while True:

    current_year += 1
    year_as_string = str(current_year)
    final_year = ''
    is_happy_year = True

    for digit in year_as_string:

        if digit in final_year:
            is_happy_year = False
            break

        final_year += str(digit)

    if is_happy_year:
        break
print(current_year)