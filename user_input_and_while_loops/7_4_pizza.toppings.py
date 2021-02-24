prompt = "\nWhat kind of pizza toppings you want to your pizza?"
prompt += "\n(When you finish, enter 'quit'): "
message = ""

while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

#Another option is:
prompt = "\nWhat kind of pizza toppings you want to your pizza?"
prompt += "\n(When you finish, enter 'quit'): "

while True:
    toppings = input(prompt)
    if toppings != 'quit':
        print(" I`ll add " + topping + " to your pizza.")
    else:
        break