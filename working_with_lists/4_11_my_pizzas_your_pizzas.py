pizzas = ['garden classic', 'margarita', 'ventricina']
for pizza in pizzas:
    print(pizza)
    print(f'The name of that pizza is "{pizza.title()}".\n')
print("I really love pizza!")
print("\n")

friend_pizzas = pizzas[:]
print(friend_pizzas)

pizzas.append('meat mania')
friend_pizzas.insert(1, 'bananas')
print(pizzas)
print(friend_pizzas)
print("\n")

print("My favorite pizzas are:")
for pizza in pizzas:
    print("- " + pizza)

print("\nMy friend`s favorite pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)

print("\nBut I really love two of them:")
for pizza in pizzas[2:4]:
    print("- " + pizza)