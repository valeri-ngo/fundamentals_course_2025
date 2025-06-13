def count_number_multiply(num_1:int, num_2:int, num_3:int) -> str:
    if num_1 == 0 or num_2 == 0 or num_3 == 0:
        return f"zero"
    negative_counter = 0

    if num_1 < 0:
        negative_counter += 1
    if num_2 < 0:
        negative_counter += 1
    if num_3 <0:
        negative_counter +=1

    if negative_counter % 2 == 0:
        return 'positive'
    elif negative_counter % 2 != 0:
        return 'negative'


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
print(count_number_multiply(number_1, number_2, number_3))