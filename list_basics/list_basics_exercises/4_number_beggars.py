money_as_string = input().split(", ")
number_of_beggars = int(input())
# money_as_integer = [int(money) for money in money_as_string]

money_as_integer = []

for current_money in money_as_string:
    money_as_integer.append(int(current_money))

final_list = []
start_of_index = 0

for current_beggar in range(number_of_beggars):
    current_beggar_sum = 0

    for index in range(start_of_index, len(money_as_integer), number_of_beggars):
        current_beggar_sum += money_as_integer[index]
    final_list.append(current_beggar_sum)
    start_of_index += 1

print(final_list)