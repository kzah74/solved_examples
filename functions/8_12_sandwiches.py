def order(*sandwich_items):
    """Print a list of items a person wants on a sandwich"""
    print(f"\nYour sandwich will be with:")
    for sandwich_item in sandwich_items:
        print(f"- {sandwich_item}")

order('meat')
order('meat', 'onion')
order('tomato', 'onion', 'papper')