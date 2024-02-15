# deli

ordered_sandwiches = ['tuna', 'salami', 'turkey', 'roastbeef']
made_sandwiches = []

while ordered_sandwiches:
    sandwich = ordered_sandwiches.pop()
    print('I am making your ' + sandwich + ' sandwich.')
    made_sandwiches.append(sandwich)
for sandwiches in made_sandwiches:
    print('I have now made your ' + sandwiches.title() + ' sandwich.')

