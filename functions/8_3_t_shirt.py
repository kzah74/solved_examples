def make_shirt(size, printed_text):
    """Display a size and the text of a message that should be printed."""
    print(f'The T-shirt is size {size.title()} with text "{printed_text}".')

make_shirt('l', 'I love books')
make_shirt(size='s', printed_text='I am the best')