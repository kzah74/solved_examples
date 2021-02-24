usernames = ['simon', 'admin', 'antony', 'mike', 'rex']

if usernames:
    for username in usernames:
        print(f"Hello, {username.title()}.")
else:
    print("We need to find some users.")

usernames = []
if usernames:
    for username in usernames:
        print(f"\nHello, {username.title()}.")
else:
    print("\nWe need to find some users.")
