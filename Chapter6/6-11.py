cities = {
    'Orlando' : {'state' : 'FL', 'population' : '1m', 'fact' : 'I was born here.'},
    'Nashville' : {'state' : 'TN', 'population' : 400000, 'fact' : 'This is home to singer/songwriters of America.'},
    'Los Angelas' : {'state' : 'CA', 'population' : '3m', 'fact' : 'Sublime was founded here.'}
    }

for city, info in cities.items():
    print('\t')
    print(city.title())
    for x, y in info.items():
        print(x.title() + ': ' + str(y))