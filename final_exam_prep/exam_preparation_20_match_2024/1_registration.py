class UsernameHandler():

    def __init__(self):
        self.username = ''
        self.commands = {
            'Letters': self.letters,
            'Reverse': self.reverse,
            'Substring': self.substring,
            'Replace': self.replace,
            'IsValid': self.is_valid
        }

    def letters(self, case_type):
        if case_type == 'Lower':
            self.username = self.username.lower()
        elif case_type == 'Upper':
            self.username = self.username.upper()
        print(self.username)

    def reverse(self, start, end):
        start = int(start)
        end = int(end)
        if 0 <= start <= end < len(self.username):
            substring = self.username[start:end + 1]
            reversed_substring = substring[::-1]
            print(reversed_substring)

    def substring(self, substr):
        if substr in self.username:
            self.username = self.username.replace(substr, '', 1)
            print(self.username)
        else:
            print(f"The username {self.username} doesn't contain {substr}.")

    def replace(self, char):
        if char in self.username:
            self.username = self.username.replace(char, '-')
            print(self.username)

    def is_valid(self, char):
        if char in self.username:
            print('Valid username.')
        else:
            print(f"{char} must be contained in your username.")

    def main(self):

        self.username = input()

        while True:

            commands = input()

            if commands == 'Registration':
                break

            command_parts = commands.split()
            action = command_parts[0]
            arguments = command_parts[1:]

            if action in self.commands:
                self.commands[action](*arguments)

if __name__ == '__main__':
    handler = UsernameHandler()
    handler.main()