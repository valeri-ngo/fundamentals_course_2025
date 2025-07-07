products = {}

while True:

    product = input()
    if product == "buy":
        break

    name, price, quantity = product.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = {'price': price, 'quantity': quantity}
    else:
        products[name]['quantity'] += quantity
        products[name]['price'] = price

for name, price in products.items():
    total_price = products[name]['price'] * products[name]['quantity']
    print(f"{name} -> {total_price:.2f}")
