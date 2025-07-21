import re

bought_items = []
total_cost = 0
pattern = r'%([A-Z][a-z]+)%[^|%$.]*<(\w+)>[^|%$.]*\|(\d+)\|[^|%$.]*?(\d+(?:\.\d+)?)\$'
command = input()

while command != 'end of shift':
    match = re.search(pattern,command)
    if match:
        sum_cost = 0
        customer, product, quantity, price = match.groups()
        bought_items.append(product)
        sum_cost += float(price) * int(quantity)
        total_cost += sum_cost
        print(f"{match.group(1)}: {product} - {sum_cost:.2f}")
    command = input()
print(f"Total income: {total_cost:.2f}")