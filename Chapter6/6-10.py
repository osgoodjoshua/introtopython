favNumbers = {
    'kelly' : [3, 7],
    'Robert' : [57],
    'antonio' : [42, 79, 35],
    'Joe' : [3],
    'Carmen' : [999999, 1]
    }

for name, numbers in favNumbers.items():
    if len(numbers) <=1:
        print(name.title() + "'s favorite number is:")
        for number in numbers:
            print('\t' + str(number))
    else:
        print(name.title() + "'s favorite numbers are: ")
        for number in numbers:
            print('\t' + str(number))
        
