def make_album(artist_name, album_title, songs=None):
    """Describing a music album"""
    information = {
    'name': artist_name.title(),
    'title': album_title.title(),
    }

    if songs:
        information['songs'] = songs
    return information

make_album('tim', 'love')

variable = make_album('andrea', 'beauty')
print(variable)

variable = make_album('queen', 'show must go on')
print(variable)

variable = make_album('kristiyan', 'the programmer')
print(variable)

variable = make_album('mike', 'nice woman', 5)
print(variable)