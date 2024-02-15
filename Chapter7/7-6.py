from collections import Counter

greeting = 'What topping would you like to add to your pizza?'
greeting += "\nEnter 'quit' when you are finished. "

order = True
message = ''
toppings = 0

while order:
    message = input(greeting)
    if message == 'quit':
        break
    elif message != 'quit':
        print(message + ' has been added to your pizza.')
        toppings += 1
        if toppings == 4:
            print('You have one topping left.')
        if toppings >= 5:
            print('You have added the maximum topping amount, your pizza is being made. 😃')
            order = False
