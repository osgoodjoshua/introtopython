#sandwich function - arbitrary arguments

def makemysandwich(*toppings):
        print('\nHere are the toppings you added to the sandwich: ')
        for topping in toppings:
                print(topping.title())

makemysandwich('lettuce', 'tomato', 'cheese')
makemysandwich('bacon', 'extra bacon')
makemysandwich('salami')