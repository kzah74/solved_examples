from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
my_ticket = '2'

winning_ticket = []
print("Let`s see what the winning ticket is...")

while my_ticket not in winning_ticket:
    pulled_item = choice(possibilities)

    if pulled_item not in winning_ticket:
        print(f"We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)