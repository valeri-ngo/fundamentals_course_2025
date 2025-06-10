# number_of_symbols = int(input())
#
# for first_symbol in range(97, 97 + number_of_symbols):
#     for second_symbol in range(97, 97 + number_of_symbols):
#         for third_symbol in range(97, 97 + number_of_symbols):
#             print(f'{chr(first_symbol)}{chr(second_symbol)}{chr(third_symbol)}')

# number_of_symbols = int(input())
# for first_symbol in range(97, 97 + number_of_symbols):
#     for second_symbol in range(97, 97 + number_of_symbols):
#         for third_symbol in range(97, 97 + number_of_symbols):
#             print(f"{chr(first_symbol)}{chr(second_symbol)}{chr(third_symbol)}")

number_of_loops = int(input())

for first_loop in range(97, 97 + number_of_loops):
    for second_loop in range(97, 97 + number_of_loops):
        for third_loop in range(97, 97 + number_of_loops):
            print(f'{chr(first_loop)}{chr(second_loop)}{chr(third_loop)}')