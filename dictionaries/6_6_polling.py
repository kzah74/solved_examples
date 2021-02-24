favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

should_take = ['mike', 'sarah', 'kristyan', 'phil', 'simon']

for name in should_take:
    if name in favourite_languages.keys():
        print(f"Thank you for your respond, {name.title()}.")
    else:
        print(f"I am inviting you to take the poll, {name.title()}.")