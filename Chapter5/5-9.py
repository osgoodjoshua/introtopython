usernames = []
#'admin', 'becky', 'john', 'debra', 'daniel'

if usernames:
    for username in usernames:
        if username == 'admin':
            print('Hello ' + username + ', what would you like to do?')
        elif username in usernames:
            print('Hi ' + username.title() + ', how are you today?')
        else:
            print("I'm sorry, that is an invalid username.")
else:
    print('Oh no, we need some users!')