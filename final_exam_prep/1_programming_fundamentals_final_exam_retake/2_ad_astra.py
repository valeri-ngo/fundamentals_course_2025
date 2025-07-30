import re

calories_per_day = 2000
days_counter = 0
sum_all_calories = 0

text_string = input()
regex_item = r'([|#])([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d{1,5})\1'
clean_items = re.finditer(regex_item, text_string)
food_lst = []

for match_lst in clean_items:
    item = match_lst.group(2)
    expiration_date = match_lst.group(3)
    calories = int(match_lst.group(4))
    sum_all_calories += calories
    food_lst.append((item, expiration_date, calories))
days_counter = sum_all_calories // calories_per_day
print(f'You have food to last you for: {days_counter} days!')

for item, expiration_date, cal in food_lst:
    print(f'Item: {item}, Best before: {expiration_date}, Nutrition: {cal}')
