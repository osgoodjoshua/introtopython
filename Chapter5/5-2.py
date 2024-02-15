car = 'green'
truck = 'Dodge'
sportscar = 'vette'
duck = ['quack', 'feathers']
island = 'water'
number = 18
myList = ['buck', 'deer', 'antelope']

print('car = green')
print(car == 'green')
print('car != green')
print(car != 'green')
print('truck = dodge')
print(truck == 'dodge')
print('truck = dodge.lower')
print(truck.lower() == 'dodge')
print('number = 18')
print(number == 18)
print('number < 18')
print(number < 18)
print('number > 18')
print(number > 18)
print('number >= 18)')
print(number >= 18)
print('number < 9')
print(number < 9)
print('number > 9')
print(number > 9)
# need to check how this function below works
print('duck == quack and feathers')
print(duck == 'quack' and 'feathers')
print('duck == quack or feathers')
print(duck == 'quack' or 'feathers')

if 'buck' in myList:
    print(True)
if 'bucks' not in myList:
    print(True)