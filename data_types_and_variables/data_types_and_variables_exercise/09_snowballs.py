number_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

for current_snowball_made in range (number_of_snowballs):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())

    current_snowball = (current_weight // current_time) ** current_quality

    if current_snowball > max_value:
        max_weight = current_weight
        max_time = current_time
        max_quality = current_quality
        max_value = current_snowball

print(f'{max_weight} : {max_time} = {max_value} ({max_quality})')