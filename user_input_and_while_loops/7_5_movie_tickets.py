prompt = "\nTell me your age and I`ll tell you the price of your ticket?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print(" Your ticket is free.")
    elif age <= 12:
        print(" Your ticket costs $10.")
    else:
        print(" Your ticket costs $15.")