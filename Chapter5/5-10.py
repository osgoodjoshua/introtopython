current_usernames = ['admin', 'becky', 'john', 'debra', 'daniel']
new_usernames = ['ADmin', 'John', 'johnathan', 'alfred']

if new_usernames:
    for username in new_usernames:
        if username.lower() in current_usernames:
            print('I am sorry ' + username.title() + ', this has already been taken.')
        elif username.lower() not in current_usernames:
            print('Hi ' + username.title() + ', thanks for signing up!')
else:
    print('Oh no, we need some users!')