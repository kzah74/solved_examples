guest_list = ['mike', 'nikolas', 'sam']
print(guest_list)
message = f"Hello, {guest_list[0].title()}, {guest_list[1].title()} and {guest_list[-1].title()}, I just found a bigger dinner table for tonight."
print(message)
guest_list.insert(0,'rex')
print(guest_list)
guest_list.insert(2, 'simon')
print(guest_list)
guest_list.append('tom')
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
message = "Hello, there, I am so sorry, but my new dinner table won`t arrive in time and I can invite only two people for dinner."
print(message)
print(guest_list)
removing_1 = 'rex'
guest_list.remove(removing_1)
print(guest_list)
message_removing_1 = f"I am so sorry, {removing_1.title()}, but I can`t invite you to dinner."
print(message_removing_1)
removing_2 = guest_list[3]
guest_list.remove(removing_2)
print(guest_list)
message_removing_2 = f"I am so sorry, {removing_2.title()}, but I can`t invite you to dinner."
print(message_removing_2)
removing_3 = 'tom'
guest_list.remove(removing_3)
print(guest_list)
message_removing_3 = f"I am so sorry, {removing_3.title()}, but I can`t invite you to dinner."
print(message_removing_3)
print(guest_list)
removing_4 = guest_list.pop(1)
print(guest_list)
message_removing_4 = f"I am so sorry, {removing_4.title()}, but I can`t invite you to dinner."
print(message_removing_4)
message_invite_1 = f"Hello, {guest_list[0].title()}, you are still invited."
print(message_invite_1)
message_invite_2 = f"Hello, {guest_list[1].title()}, you are still invited."
print(message_invite_2)
del guest_list[0]
del guest_list[0]
print(guest_list)
