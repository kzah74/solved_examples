guest_list = ['mike', 'nikolas', 'sam']
message = f"Hello, {guest_list[0].title()}, I am inviting you to dinner."
print(message)
message = f"Hello, {guest_list[1].title()}, I am inviting you to dinner."
print(message)
message = f"Hello, {guest_list[-1].title()}, I am inviting you to dinner."
print(message)
print(len(guest_list))
message = f"Hello, {guest_list[0].title()}, {guest_list[1].title()} and {guest_list[-1].title()}, you are inviting to dinner and we will be {len(guest_list)} people at the dinner except me."
print(message)
