guest_list = ['Jesus', 'grandma', 'Sylvestor Stalone', 'daffy duck and friends']
message = ', would you like to go to dinner with me?'

print(guest_list[0] + message.strip('?') + ' Lord?')
print('\n\t' + guest_list[1].title() + message)
print('\n\t\t' + guest_list[2] + message)
print('\n\t\t\t' + guest_list[3].upper() + message)
print('\n' + guest_list[2] + ', unfortunately can not make it.')

del guest_list[2]
guest_list.insert(2, 'Joe Jackson')
print('\n')

print(guest_list[0] + message.strip('?') + ' Lord?')
print('\n\t' + guest_list[1].title() + message)
print('\n\t\t' + guest_list[2] + message)
print('\n\t\t\t' + guest_list[3].upper() + message)
