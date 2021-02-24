guest_list = ['mike', 'simon', 'antony']
print(guest_list)
message = f"Hello, {guest_list[0].title()}, {guest_list[1].title()} and {guest_list[-1].title()}, I just found a bigger dinner table for tonight."
print(message)
guest_list.insert(0,'rex')
print(guest_list)
guest_list.insert(2, 'tommy')
print(guest_list)
guest_list.append('boris')
print(guest_list)
message_1 = f"Hello, {guest_list[0].title()}, I am inviting you for dinner tonight."
message_2 = f"Hello, {guest_list[1].title()}, I am inviting you for dinner tonight."
message_3 = f"Hello, {guest_list[2].title()}, I am inviting you for dinner tonight."
message_4 = f"Hello, {guest_list[3].title()}, I am inviting you for dinner tonight."
message_5 = f"Hello, {guest_list[4].title()}, I am inviting you for dinner tonight."
message_6 = f"Hello, {guest_list[5].title()}, I am inviting you for dinner tonight."
print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)
print(message_6)
