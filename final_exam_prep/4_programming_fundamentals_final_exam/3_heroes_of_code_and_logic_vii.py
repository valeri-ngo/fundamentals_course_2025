def cast_spell(hero_info: dict, hero_name: str, mp_needed: int, spell_name: str):
    mana_pts = hero_info[hero_name]['mana_pts']
    if mana_pts >= mp_needed:
        mana_pts -= mp_needed
        hero_info[hero_name]['mana_pts'] = mana_pts
        print(f'{hero_name} has successfully cast {spell_name} and now has {mana_pts} MP!')
    else:
        print(f'{hero_name} does not have enough MP to cast {spell_name}!')

def take_damage(hero_info: dict, hero_name: str, damage: int, attacker: str):
    current_hp = hero_info[hero_name]['hit_pts']
    current_hp -= damage
    if current_hp <= 0:
        print(f'{hero_name} has been killed by {attacker}!')
        del hero_info[hero_name]
    else:
        hero_info[hero_name]['hit_pts'] = current_hp
        print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!')

def recharge(hero_info: dict, hero_name: str, amount_mp_recharged: int):
    mana_pts = hero_info[hero_name]['mana_pts']
    actual_mp_recharged = min(amount_mp_recharged, 200 - mana_pts)
    mana_pts += actual_mp_recharged
    hero_info[hero_name]['mana_pts'] = mana_pts
    print(f'{hero_name} recharged for {actual_mp_recharged} MP!')

def heal(hero_info: dict, hero_name:str, amount_hp_recharged: int):
    hit_pts = hero_info[hero_name]['hit_pts']
    actual_hp_recharged = min(amount_hp_recharged, 100 - hit_pts)
    hit_pts += actual_hp_recharged
    hero_info[hero_name]['hit_pts'] = hit_pts
    print(f'{hero_name} healed for {actual_hp_recharged} HP!')

hero_info = {}

def main():
    number_of_heroes = int(input())

    for _ in range(number_of_heroes):

        current_hero = input().split()
        current_hero_name = current_hero[0]
        hit_pts = int(current_hero[1])
        mana_pts = int(current_hero[2])

        if current_hero_name not in hero_info:
            hero_info[current_hero_name] = {'hit_pts': hit_pts,
                                            'mana_pts': mana_pts
                                            }

    while True:

        command = input()

        if command == 'End':
            break

        parts = command.split(' - ')
        current_action = parts[0]

        if current_action == 'CastSpell':
            hero_name = parts[1]
            mp_needed = int(parts[2])
            spell_name = parts[3]
            cast_spell(hero_info, hero_name, mp_needed, spell_name)

        elif current_action == 'TakeDamage':
            hero_name = parts[1]
            damage = int(parts[2])
            attacker = parts[3]
            take_damage(hero_info, hero_name, damage, attacker)

        elif current_action == 'Recharge':
            hero_name = parts[1]
            amount_mp_recharged = int(parts[2])
            recharge(hero_info, hero_name, amount_mp_recharged)

        elif current_action == 'Heal':
            hero_name = parts[1]
            amount_hp_recharged = int(parts[2])
            heal(hero_info, hero_name, amount_hp_recharged)
    for hero, stats in hero_info.items():
        print(hero)
        print(f"  HP: {stats['hit_pts']}")
        print(f"  MP: {stats['mana_pts']}")

if __name__ == '__main__':
    main()