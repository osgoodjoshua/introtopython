prompt = ('What is your age? ')


while True:
    age = int(input(prompt))
    if age <= 3:
        print('Your ticket is free.')
    elif age <= 12:
        print('Your ticket is 12 dollars.')
    elif age <= 99:
        print('Your tickets is 15 dollars.')
    else:
        print('You are too old.')
        break


