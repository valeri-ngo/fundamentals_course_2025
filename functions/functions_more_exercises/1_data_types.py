def data_type(data_input:str, value:str):

    if data_input == 'int':
        return int(value) * 2
    elif data_input == 'real':
        return f'{float(value) * 1.5:.2f}'
    elif data_input == 'string':
        return f'${value}$'
    else:
        return None

string = input()
number = input()
result = data_type(string, number)
print(result)