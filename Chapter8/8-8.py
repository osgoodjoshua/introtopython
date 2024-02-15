def favMusicAlbum(artist, album):
    formatted = {'Artist Name' : artist, 'Album Name' : album}
    return str(formatted).title()

while True:
    print('I want to know you better.' + '\nEnter "q" to quit at any time.')
    userArtist = input('Who is your favorite artist? ')
    if userArtist == 'q':
        break
    userAlbum = input('What is your favorite album by them? ')
    if userAlbum == 'q':
        break
    favMusic = favMusicAlbum(userArtist, userAlbum)
    print('This is your favorite music: ' + str(favMusic))
    print("Let's do it again!\n")

