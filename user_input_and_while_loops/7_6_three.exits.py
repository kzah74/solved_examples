prompt = "\nTell me your age and I`ll tell you the price of your ticket?"
prompt += "\nEnter 'quit' when you are finished. "

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    age = int(age)

    if age < 3:
        print(" Your ticket is free.")
    elif age <= 12:
        print(" Your ticket costs $10.")
    else:
        print(" Your ticket costs $15.")


prompt = "\nTell me your age and I`ll tell you the price of your ticket?"
prompt += "\nEnter 'quit' when you are finished. "

active = True
while active:
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