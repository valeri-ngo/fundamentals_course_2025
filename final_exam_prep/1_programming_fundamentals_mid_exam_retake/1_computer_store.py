def is_float(num_str: str) -> bool:
    if num_str.count('.') <= 1:
        parts = num_str.split('.')
        if all(current_part.isdigit() for current_part in parts if current_part != ''):
            return True

    return False

prices_for_parts = []

while True:
    price_parts = input().strip()

    if price_parts == 'special':
        customer_type = 'special'
        break
    elif price_parts == 'regular':
        customer_type = 'regular'
        break
    else:
        if is_float(price_parts):
            current_price = float(price_parts)
            if current_price <= 0:
                print('Invalid price!')
            else:
                prices_for_parts.append(current_price)
        else:
            print('Invalid price!')
if not prices_for_parts:
    print('Invalid order!')
else:
    total_without_tax = sum(prices_for_parts)
    total_with_tax = total_without_tax * 0.2
    total = total_without_tax + total_with_tax

    if customer_type == 'special':
        total *= 0.9

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_without_tax:.2f}$")
    print(f"Taxes: {total_with_tax:.2f}$")
    print("-----------")
    print(f"Total price: {total:.2f}$")