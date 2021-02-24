guest_list = ['mike', 'simon', 'antony']
print(guest_list)
can_not_come = 'antony'
guest_list.remove(can_not_come)
print(guest_list)
guest_list.append('rex')
print(guest_list)
message = f"Hello, {guest_list[0].title()}, I am inviting you to dinner tonight."
print(message)
message = f"Hello, {guest_list[1].title()}, I am inviting you to dinner tonight."
print(message)
message = f"Hello, {guest_list[-1].title()}, I am inviting you to dinner tonight."
print(message)
message_1 = f"Hello, {guest_list[0].title()}, I am inviting you to dinner tonight."
message_2 = f"Hello, {guest_list[1].title()}, I am inviting you to dinner tonight."
message_3 = f"Hello, {guest_list[-1].title()}, I am inviting you to dinner tonight."
print(message_1)
print(message_2)
print(message_3)
