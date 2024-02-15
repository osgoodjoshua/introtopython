#passing lists

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for magician in magicians:
        newtitle = 'The Great ' + magician
        greatMagicians.append(newtitle)

magicians = ['Todd', 'Kelly', 'Michael']
greatMagicians = []

show_magicians(magicians)
make_great(magicians)
show_magicians(greatMagicians)

