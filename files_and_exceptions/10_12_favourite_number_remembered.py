import json

def get_stored_number():
    """Get stored number if available."""
    filename = 'favourite_number.json'
    try:
        with open(filename) as f:
            favourite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favourite_number

def get_new_number():
    """Prompt for a new number"""
    favourite_number = int(input("Tell me your favourite number: "))
    filename = 'favourite_number.json'
    with open(filename, 'w') as f:
        json.dump(favourite_number, f)
    return favourite_number

def print_number():
    """Printing the number."""
    favourite_number = get_stored_number()
    if favourite_number:
        print(f"I know your favourite number! It`s {favourite_number}.")
    else:
        favourite_number = get_new_number()
        print("I will remember your favourite number.")

print_number()