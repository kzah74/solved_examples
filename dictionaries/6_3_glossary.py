glossary = {
    'string': 'A series of characters',
    'comment': 'A note in a program that the Python interpreter ignores',
    'list': 'A collection of items in a particular order',
    'loop': 'Work through a collection of items, one at a time',
    'dictionary': 'A collection of key-value pairs',
}

word = 'string'
print("- " + word.title() + " is: " + glossary['string'].lower() + ".")

word = 'comment'
print("\n- " + word.title() + " is: " + glossary['comment'].lower() + ".")

word = 'list'
print("\n- " + word.title() + " is: " + glossary['list'].lower() + ".")

word = 'loop'
print("\n- " + word.title() + " is: \n\t" + glossary['comment'].lower() + ".")

word = 'dictionary'
print("\n- " + word.title() + " is: \n\t" + glossary['dictionary'].lower() + ".")
print("\n")