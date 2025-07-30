import re

barcode_numbers = int(input())
valid_barcode = r'@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+'

for _ in range(barcode_numbers):
    string = input()
    match = re.search(valid_barcode, string)

    if not match:
        print('Invalid barcode')
    else:
        product = match.group(1)
        digits = re.findall(r'\d', product)

        if digits:
            product_group = ''.join(digits)
        else:
            product_group = '00'

        print(f'Product group: {product_group}')