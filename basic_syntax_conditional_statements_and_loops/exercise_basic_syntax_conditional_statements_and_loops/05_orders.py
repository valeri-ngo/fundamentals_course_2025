number_of_orders = int(input())
total_price = 0

for _ in range (number_of_orders):

    price_per_coffee = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if price_per_coffee < 0.01 or price_per_coffee > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue

    sum_per_order = (price_per_coffee * days) * capsules_per_day
    total_price += sum_per_order

    print(f'The price for the coffee is: ${sum_per_order:.2f}')

print(f'Total: ${total_price:.2f}')
