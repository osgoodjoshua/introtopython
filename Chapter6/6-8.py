barky = {
    'sound' : 'bark',
    'color' : 'black and white',
    'owner' : 'John',
    'weight' : '140lbs',
    'type' : 'dog'
    }
sparky = {
    'sound' : 'gloop',
    'color' : 'gold and white',
    'owner' : 'Joshua',
    'weight' : '10oz',
    'type' : 'goldfish'
    }
purry = {
    'sound' : 'meow',
    'color' : 'calico',
    'owner' : 'Carmen',
    'weight' : '10lbs',
    'type' : 'cat'
    }
pets = [barky, sparky, purry]

for pet in pets:
    print('\t')
    for x, y in pet.items():
        print(x.title() + ': ' + y.title())