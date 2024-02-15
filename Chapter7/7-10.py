#vacation poll

userpoll = {}
name = 'What is your name '
city = 'What city would you like to visit? '
polling = True

while polling:
    names = input(name)
    responses = input(city)
    userpoll[names] = responses
    repeat = input('Would another person like to respond? Y/N ')
    if repeat == 'N' or 'n':
        polling = False

print('\n--- POLLING RESULTS ---')
for x, y in userpoll.items():
    print(str(x).title() + ' would like to visit ' +
          str(y).title() + '.')
    




    