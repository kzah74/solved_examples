sandwich_orders = ['tuna', 'pastrami', 'vegetarian', 'pastrami', 'meat', 
                    'pastrami']
finished_sandwiches = []

message = "The Deli has run out of pastrami."
print(message)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am working on your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)
    
print("\n")
for sandwich in finished_sandwiches:
    print(f"I made your {sandwich} sandwich.")

