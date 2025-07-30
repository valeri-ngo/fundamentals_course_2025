class Inventory():

    def __init__(self):
        self.items = []

        self.commands = {'Collect': self.collect,
                         'Drop': self.drop,
                         'Combine Items': self.combine,
                         'Renew': self.renew
                         }

    def collect(self, item):
        if item not in self.items:
            self.items.append(item)

    def drop(self,item):
        if item in self.items:
            self.items.remove(item)

    def combine(self, old_item, new_item):
        if old_item in self.items:
            place = self.items.index(old_item)
            self.items.insert(place +1, new_item)

    def renew(self, item):
        if item in self.items:
            self.items.remove(item)
            self.items.append(item)

    def main(self):
        self.items = input().split(', ')

        while True:
            command = input()

            if command == 'Craft!':
                break

            action, *arguments = command.split(' - ')
            if action not in self.commands:
                continue

            if action in self.commands:
                if action == 'Combine Items' and arguments:
                    old_item, new_item = arguments[0].split(':')
                    self.commands[action](old_item, new_item)
                elif arguments:
                    self.commands[action](arguments[0])

        print(', '.join(self.items))

if __name__ == '__main__':
    inventory = Inventory()
    inventory.main()