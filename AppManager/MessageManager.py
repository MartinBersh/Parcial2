class MessageManager:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, recipient, message):
        new_message = {
            'sender': sender,
            'recipient': recipient,
            'message': message
        }
        self.messages.append(new_message)

    def get_messages(self, user):
        return [message for message in self.messages if message['sender'] == user or message['recipient'] == user]
