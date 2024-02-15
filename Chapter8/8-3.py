#positional and keyword arguments

def makeshirt(size, message):
    print('\nYou have ordered a ' + size + ' shirt.')
    print('Your shirt will say: ' + message)

makeshirt('L', 'I want food.')
makeshirt(size= 'XL', message= 'This is new.')