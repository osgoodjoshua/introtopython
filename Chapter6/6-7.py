person1 = {
    'firstName' : 'John',
    'lastName' : 'Osgood',
    'hairColor' : 'brn',
    'birthCity' : 'Orlando',
    'height' : 6
    }
person2 = {
    'firstName' : 'Joshua',
    'lastName' : 'Osgood',
    'hairColor' : 'blk',
    'birthCity' : 'Orlando',
    'height' : 5.11
    }
person3 = {
    'firstName' : 'Gemma',
    'lastName' : 'Osgood',
    'hairColor' : 'blnd',
    'birthCity' : 'Church Point',
    'height' : 5.2
    }

people = [person1, person2, person3]

# for p in people:
#     print(p.values())

for p in people:
    print('\t')
    for x, y in p.items():
        print(x.title() + ': ', y)

