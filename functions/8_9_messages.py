def show_messages(messages):
    """Print a series of short text messages."""
    for message in messages:
        print(f"{message.title()}.")

messages = ['hey there', 'hello there', 'how are you']
show_messages(messages)
