current_users = ['simon', 'anThony', 'rex', 'mike', 'nadya']
new_users = ['vyara', 'petya', 'hilda', 'Anthony', 'enrico']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'Sorry, the username "{new_user}" is taken.')
    else:
        print(f'Great, the username "{new_user}" is still available.')
