number = int(input())

for _ in range(number):
    data_input = input()
    start_name = data_input.find('@') + 1
    end_name = data_input.find('|')
    name = data_input[start_name:end_name]

    start_age = data_input.find('#') +1
    end_age = data_input.find('*')
    age = data_input[start_age:end_age]

    print(f"{name} is {age} years old.")