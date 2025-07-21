# import re
#
# input_string = input()
#
# demon_names = [name.strip() for name in input_string.split(',')]
# results = []
#
# damage_pattern = r'[-+]?\d+(?:\.\d+)?'
# health_pattern = r'([^0-9+\-\*\/\.])'
# for demon in sorted(demon_names):
#     health_value = 0
#     health = re.findall(health_pattern, demon)
#     for char in health:
#         health_value += ord(char)
#
#     damage_values = re.findall(damage_pattern, demon)
#     dmg_value = 0
#     for dmg in damage_values:
#         dmg_value += float(dmg)
#
#     for symbol in demon:
#         if symbol == '*':
#             dmg_value *= 2
#         elif symbol == '/':
#             dmg_value /= 2
#
#     results.append(f'{demon} - {health_value} health, {dmg_value:.2f} damage')
# for result in results:
#     print(result)

def calculate_health(demon_name):
    health_pattern = r'[^0-9+\-*/.]'
    return sum(ord(char) for char in re.findall(health_pattern, demon_name))


def calculate_damage(demon_name):
    damage_pattern = r'[-+]?\d+(?:\.\d+)?'
    base_damage = sum(float(d) for d in re.findall(damage_pattern, demon_name))

    for symbol in demon_name:
        if symbol == '*':
            base_damage *= 2
        elif symbol == '/':
            base_damage /= 2

    return base_damage
input_string = input()
demon_names = [name.strip() for name in input_string.split(',')]
results = []

for demon in sorted(demon_names):
    health = calculate_health(demon)
    damage = calculate_damage(demon)
    results.append(f'{demon} - {health} health, {damage:.2f} damage')

for result in results:
    print(result)
