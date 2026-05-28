def send_messages(messages):
    """
    Tells if the message has been send.
    Move each message to sent_messages after printing.
    """
    while messages:
        message = messages.pop()
        print(f"The message '{message}' has been succesfully send.")
        sent_messages.append(message)

unsend_messages= ["Hello World!", "Your are so salty", "I cant drink milk :("]
sent_messages = []

send_messages(unsend_messages)
print(f"The list of unsend messages has been updated to:\n{unsend_messages}")
print(f"The list of sent messages has been updated to:\n{sent_messages}")