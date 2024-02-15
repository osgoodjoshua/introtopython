favLanguages = {
    'kelly' : 'python',
    'john' : 'c++',
    'andrew' : 'javascript',
    'alan' : 'ruby'
    }

newPoll = ['john', 'kelly', 'randy', 'stephen']

for user in favLanguages.keys():
    if user in newPoll:
        print('Thank you, ' + user.title() + ' for taking the poll.')
    else:
        print(user.title() + ', please consider taking our poll.')

