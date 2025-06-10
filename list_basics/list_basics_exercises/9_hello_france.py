collection_of_items = input().split('|')
budget = float(input())

bought_items = []

maximum_price_for_cloths = 50.00        ## Maximum price for cloths
maximum_price_for_shoes = 35.00     ## Maximum price for shoes
maximum_price_for_accessories = 20.50       ## Maximum price for accessories

ticket = 150        ## Ticket price
profit = 0

markup_price = []

for items in collection_of_items:
    item = items.split('->')
    type_of_item = item[0]
    value_of_item = float(item[1])

    if type_of_item == 'Clothes' and value_of_item > maximum_price_for_cloths:
        continue
    elif type_of_item == 'Shoes' and value_of_item > maximum_price_for_shoes:
        continue
    elif type_of_item == 'Accessories' and value_of_item > maximum_price_for_accessories:
        continue

    if budget >= value_of_item:
        budget -= value_of_item
        bought_items.append(value_of_item)
        price_after_markup = value_of_item * 1.4
        markup_price.append(price_after_markup)
        profit += price_after_markup - value_of_item

for price in markup_price:
    print(f'{price:.2f}', end= ' ')
print()
print(f"Profit: {profit:.2f}")

if sum(markup_price) + budget >= ticket:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')
