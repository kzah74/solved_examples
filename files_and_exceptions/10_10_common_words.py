filename = 'little_women.txt'

with open(filename) as f:
    content = f.read()
    words = content.split()
    print(len(words))

count = words.count('and')
print(count)
print(f"The word 'and' appears in '{filename}' {count} times.\n")


# Another approach.
def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    # Note: This is a really simple approximation, and the number returned
    # will be higher than the actual count.
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)

        msg = f"'{word}' appears in '{filename}' about {word_count} times."
        print(msg)

filename = 'alice.txt'
# Here, it will also count words such as 'then' and 'there'.
count_common_words(filename, 'the')
# Here, it will be with a space after 'the'.
count_common_words(filename, 'the ')