class Player():

    def __init__(self):
        self.health_points = 100
        self.bitcoins = 0

    def heal(self, amount):
        healed = min(100 - self.health_points, amount)
        self.health_points += healed
        print(f"You healed for {healed} hp.")
        print(f"Current health: {self.health_points} hp.")

    def take_damage(self, amount):
        self.health_points -= amount

    def is_alive(self):
        return self.health_points > 0

def handle_potion(player, amount):
    player.heal(amount)

def handle_chest(player, amount):
    player.bitcoins += amount
    print(f"You found {amount} bitcoins.")

class Room:

    def __init__(self, action, amount):
        self.action = action
        self.amount = int(amount)

def handle_monster(player, monster, damage, room_number):
    player.take_damage(damage)

    if player.is_alive():
        print(f"You slayed {monster}.")
        return True
    else:

        print(f"You died! Killed by {monster}.")
        print(f"Best room: {room_number}")
        return False

def run_dungeon(dungeon_string):

    player = Player()
    rooms = [Room(*r.split()) for r in dungeon_string.split('|')]

    handlers = {
        "potion": handle_potion,
        "chest": handle_chest,
    }

    for number, room in enumerate(rooms, 1):

        if room.action in handlers:
            handlers[room.action](player, room.amount)

        else:
            if not handle_monster(player, room.action, room.amount, number):
                return

    print(f"You've made it!")
    print(f"Bitcoins: {player.bitcoins}")
    print(f"Health: {player.health_points}")

if __name__ == '__main__':
    dungeon_input = input()
    run_dungeon(dungeon_input)