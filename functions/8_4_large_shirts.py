def make_shirt(size='large', printed_text='I love Python'):
    """Display a size and the text of a message that should be printed."""
    print(f'The T-shirt is size {size.title()} with text "{printed_text}".')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'I love animals')
make_shirt(size='medium', printed_text='I am the best')
make_shirt('large', printed_text='Simon loves books')