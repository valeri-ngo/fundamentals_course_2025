materials = {"shards": 0,
             "fragments": 0,
             "motes": 0,}
got_legendary_item = False

while not got_legendary_item:
    current_item = input().split()

    for index in range(0, len(current_item), +2):
        value = int(current_item[index])
        key = current_item[index +1].lower()
        if key not in materials.keys():
            materials[key] = 0
        materials[key] += value

        if materials["shards"] >= 250:
            materials["shards"] -= 250
            print(f"Shadowmourne obtained!")
            got_legendary_item = True
        elif materials["fragments"] >= 250:
            materials["fragments"] -= 250
            print(f"Valanyr obtained!")
            got_legendary_item = True
        elif materials["motes"] >= 250:
            materials["motes"] -= 250
            print(f"Dragonwrath obtained!")
            got_legendary_item = True
        if got_legendary_item:
            break
for material,quantity in materials.items():
    print(f"{material}: {quantity}")
