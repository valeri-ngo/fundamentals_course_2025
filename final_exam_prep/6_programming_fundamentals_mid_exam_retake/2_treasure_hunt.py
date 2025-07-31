class TreasureChest:

    def __init__(self, initial_loot):
        self.chest = initial_loot.split('|')
        self.command_dict = {
            'Loot': self.loot,
            'Drop': self.drop,
            'Steal': self.steal
        }

    def loot(self, items: list[str]):
        for item in items:
            if item not in self.chest:
                self.chest.insert(0, item)

    def drop(self, index: int):
        if 0 <= index < len(self.chest):
            item = self.chest.pop(index)
            self.chest.append(item)

    def steal(self, count: int) -> list[str]:
        stolen_loot = []
        if count >= len(self.chest):
            stolen_loot = self.chest[:]
            self.chest.clear()
        else:
            for _ in range(count):
                stolen_loot.insert(0, self.chest.pop())
        return stolen_loot

    def average_gain(self) -> float:
        if not self.chest:
            return 0
        total_length = sum(len(item) for item in self.chest)
        return total_length / len(self.chest)

    def main(self):

        while True:
            command = input()

            if command == 'Yohoho!':
                break

            action, *arguments = command.split()

            if action in self.command_dict:
                if action == 'Loot':
                    self.command_dict[action](arguments)
                elif action == 'Drop':
                    index = int(arguments[0])
                    self.command_dict[action](index)
                elif action == 'Steal':
                    count = int(arguments[0])
                    stolen = self.command_dict[action](count)
                    print(', '.join(stolen))

        average_treasure_gain = self.average_gain()
        if average_treasure_gain > 0:
            print(f'Average treasure gain: {self.average_gain():.2f} pirate credits.')
        else:
            print("Failed treasure hunt.")

if __name__ == '__main__':
    initial_loot = input()
    result = TreasureChest(initial_loot)
    result.main()