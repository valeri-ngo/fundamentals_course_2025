current_version = input()
my_list = current_version.split('.')
my_list = [int(num) for num in my_list]
my_list[-1] += 1

for number in range(len(my_list) -1, -1, -1):
    if my_list[number] > 9:
        my_list[number] = 0
        if number > 0:
            my_list[number -1] += 1
        else:
            my_list.insert(0, 1)
print('.'.join(str(num) for num in my_list))