# Album with while loop
def make_album(artist, title):
    """Display info about an album in a dictionary"""
    album_info = {"artist": artist, "title": title}
    return album_info

while True:
    print(f"Hi!!\nWe need some information about ur favourite music album\n If u dont want to answer write 'quit' please: ")
    a_artist = input("Album Artist: ")
    if a_artist == "quit":
        break
    
    a_title = input("Album Title: ")
    if a_title == "quit":
        break
    
    album = make_album(a_artist, a_title)
    print(album)