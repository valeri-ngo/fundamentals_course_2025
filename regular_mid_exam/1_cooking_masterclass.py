import math

budget = float(input())
students = int(input())
price_for_flour = float(input())
price_per_egg = float(input())
price_for_apron = float(input())

total_aprons = math.ceil(students * 1.2)

apron_price = total_aprons * price_for_apron
eggs_price = students * 10 * price_per_egg
free_flour_packages = students // 5
flour_price = (students - free_flour_packages) * price_for_flour

total_price = apron_price + eggs_price + flour_price

if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    needed_money = total_price - budget
    print(f"{needed_money:.2f}$ more needed.")
