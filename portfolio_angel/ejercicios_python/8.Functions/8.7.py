def make_album(artist, title):
    """Display info about an album in a dictionary"""
    album_info = {"artist": artist, "title": title}
    return album_info

album = make_album("Michale Jackson", "Thriller")
print(album)

album = make_album("Melendi", "Sin noticias de Holanda")
print(album)

# Adding number of songs
def make_album(artist, title, songs=None):
    """Display info about an album in a dictionary"""
    album_info = {"artist": artist, "title": title}
    if songs:
        album_info["songs"] = songs
    return album_info

album = make_album("Michale Jackson", "Thriller")
print(album)

album = make_album("Melendi", "Sin noticias de Holanda")
print(album)

album = make_album("Estopa", "Como el vino tinto", 12)
print(album)