# no pastrami

ordered_sandwiches = ['pastrami', 'tuna', 'pastrami', 'salami', 'turkey', 'pastrami', 'roastbeef']
made_sandwiches = []

print('Sorry, we just ran out of pastrami.')
while 'pastrami' in ordered_sandwiches:
        ordered_sandwiches.remove('pastrami')
        
while ordered_sandwiches:
    sandwich = ordered_sandwiches.pop()
    print('I am making your ' + sandwich + ' sandwich.')
    made_sandwiches.append(sandwich)
for sandwiches in made_sandwiches:
    print('I have now made your ' + sandwiches.title() + ' sandwich.')

