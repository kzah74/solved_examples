def make_album(artist_name, album_title, songs=None):
    """Describing a music album"""
    information = {
    'name': artist_name.title(),
    'title': album_title.title(),
    }

    if songs:
        information['songs'] = songs
    return information

while True:
    print("Give us the next information. \nFor exit, enter 'quit' at any time")

    a_name = input("What is the name of the artist? ")
    if a_name == 'quit':
        break

    a_title = input("What is the title of the album? ")
    if a_title == 'quit':
        break

    make_album_2 = make_album(a_name.title(), a_title.title())
    print(make_album_2)
    print("\nThank you for responding!")