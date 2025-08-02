class ActivationKeys:

    def __init__(self):
        self.key = ''
        self.commands = {'Contains': self.contains,
                         'Flip': self.flip,
                         'Slice': self.slice,
                         }

    def contains(self, substring):
        if substring in self.key:
            return f"{self.key} contains {substring}"
        else:
            return 'Substring not found!'

    def flip(self, case_type, start, end):
        start = int(start)
        end = int(end)
        part = self.key[start:end]

        if case_type == 'Lower':
            part = part.lower()
        elif case_type == 'Upper':
            part = part.upper()

        self.key = self.key[:start] + part + self.key[end:]
        return self.key

    def slice(self, start, end):
        start = int(start)
        end = int(end)
        self.key = self.key[:start] + self.key[end:]
        return self.key

    def main(self):

        self.key = input()

        while True:

            command = input()

            if command == 'Generate':
                break

            action, *arguments = command.split('>>>')
            if action not in self.commands:
                continue

            result = self.commands[action](*arguments)
            if result:
                print(result)

        print(f"Your activation key is: {self.key}")

if __name__ == '__main__':
    activation = ActivationKeys()
    activation.main()
