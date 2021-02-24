def send_messages(messages):
    """Print a series of short text messages and move to a new list."""
    while messages:
        for message in messages:
            current_message = messages.pop()
            print(f"{current_message.title()}.")
            sent_messages.append(current_message)

messages = ['hey there', 'hello there', 'how are you']
sent_messages = []

send_messages(messages[:])

print(messages)
print(sent_messages)
