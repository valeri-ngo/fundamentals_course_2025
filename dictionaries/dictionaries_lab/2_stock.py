elements = input().split()
storage = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    storage[key] = int(value)

search = input().split()

for product in search:
    if product in storage:
        print(f"We have {storage[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")