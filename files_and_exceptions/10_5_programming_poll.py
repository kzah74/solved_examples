filename = 'programming_poll.txt'
responses = []

while True:
    response = input("Why you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to continue? (yes/no): ")
    if continue_poll == 'no':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")
