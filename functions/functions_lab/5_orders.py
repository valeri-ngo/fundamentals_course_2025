def orders(order:str, number: int):
    return {'coffee': 1.50 * number ,
            'water': 1.00 * number ,
            'coke': 1.40 * number ,
            'snacks': 2.00 * number
    }.get(order)

current_order = input()
order_count = int(input())

result = orders(current_order, order_count)
print(f'{result:.2f}')
