#dictionary return

def make_album(name, album, year= ''):
    """returning a dictionary for artist album information"""
    info = {'Name' : name, 'album' : album}
    if year:
        info['year'] = year
    return info

discography = make_album('Pink Floyd', 'The Wall')
print(discography)
discography = make_album('The JOB', 'Dream Catcher', '2020')
print(discography)