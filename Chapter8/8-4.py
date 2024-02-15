#positional and keyword arguments - with defaults

def makeshirt(size = 'L', message = 'I love Python!'):
    print('\nYou have ordered a ' + size + ' shirt.')
    print('Your shirt will say: ' + message)

makeshirt()
makeshirt(size= 'M')
makeshirt('S', 'I love Jesus!')