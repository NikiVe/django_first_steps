class Person:
    def __init__(self, name):
        self.name = name


class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender.name} says to {self.receiver.name}: {self.content}. Send: {self.is_sent}"


class MailBox:
    def __init__(self):
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)

    def send_emails(self, indexes):
        for i in indexes:
            self.emails[i].send()

    def get_all_emails_info(self):
        all_info = ""
        for email in self.emails:
            all_info += f"{email.get_info()}\n"
        return all_info


mailbox = MailBox()


while True:
    command = input()
    if command == "Stop":
        break
    sender_name, receiver_name, content = command.split(" ", maxsplit=2)
    sender = Person(sender_name)
    receiver = Person(receiver_name)
    email = Email(sender, receiver, content)
    mailbox.add_email(email)

send_indexes = [int(i.strip()) for i in input().split(",")]
mailbox.send_emails(send_indexes)
print(mailbox.get_all_emails_info())
