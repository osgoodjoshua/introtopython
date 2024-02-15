#conditional tests

car = 'green'
truck = 'dodge'
sportscar = 'vette'
duck = ['quack', 'feathers']
island = 'water'

print('Does car == green? I predict True')
print(car == 'green')

print('\nDoes car == blue? I predict False')
print(car == 'blue')

print('\nDoes truck == dodge? I predict True')
print(truck == 'dodge')

print('\nDoes truck == Ford? I predict False')
print(truck == 'Ford')

print('\nDoes sportscar == corvette? I predict False')
print(sportscar == 'corvette')

print('\nDoes sportscar == vette? I predict True')
print(sportscar == 'vette')

print('\nDoes duck == quack OR feathers? I predict True')
if duck == 'quack' or 'feathers':
    print(True)

# Not sure why the below function isn't working the way I planned... Need to research more
print('\nDoes duck equal quack AND feathers? I predict True')
if duck == 'quack' and 'feathers':
    print(True)

# print('\nDoes water == island? I predict error')
# print(water == island)

print('\nDoes island == WATER? I predict False')
print(island == 'WATER')