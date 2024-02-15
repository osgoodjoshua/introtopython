pizzas = ['pepperoni', 'cheese', 'ham & pineapple', 'sausage']

friendPizzas = pizzas[:]

pizzas.append('veggie')
friendPizzas.append('alfredo')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('My friends favorite pizzas are:')
for pizza in friendPizzas:
    print(pizza)

