filename = 'guest.txt'

prompt = "Please, tell me your name. "
prompt += "\nEnter 'q' to quit: "

while True:
    response = input(prompt)
    if response == 'q':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"'{response.title()}' just vidited.\n")
        print(f"Wellcome, {response.title()}, you`ve been added to the guest book.\n")
