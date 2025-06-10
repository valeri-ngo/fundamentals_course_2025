number_of_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_repair = 0
sword_repair = 0
shield_repair = 0
armor_repair = 0

for lost_fight in range(1, number_of_fights +1):

    if lost_fight % 2 == 0:
        helmet_repair += 1

    if lost_fight % 3 == 0:
        sword_repair += 1

    if lost_fight % 2 == 0 and lost_fight % 3 == 0:
        shield_repair += 1

        if shield_repair % 2 == 0:
            armor_repair += 1

total_price_for_repair = helmet_repair * helmet_price + \
                         sword_repair * sword_price + \
                         shield_repair * shield_price + \
                         armor_repair * armor_price
print(f'Gladiator expenses: {total_price_for_repair:.2f} aureus')