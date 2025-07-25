class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'

emails = []

while (data:= input()) != "Stop":
    sender_, receiver_, content_ = data.split()
    email = Email(sender_, receiver_, content_)
    emails.append(email)

    if data == 'Stop':
        break
indices = list(map(int, input().split(", ")))

for index in indices:
    emails[index].send()

for email in emails:
    print(email.get_info())