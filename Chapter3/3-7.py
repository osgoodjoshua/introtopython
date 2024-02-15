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
print('\nLooks like a bigger table is available! \n\n\n')

guest_list.insert(0, 'tommy pickles')
guest_list.insert(3, 'Rachel')
guest_list.append('Lara Croft')

print(str(guest_list[0].title() + ', ') + str(guest_list[3] + ', and ') + str(guest_list[-1]) + ' have been added to the list. \n')

print(guest_list[0] + message)
print('\n\t' + guest_list[1].title() + message.strip('?') + ' Lord?')
print('\n\t\t' + guest_list[2] + message)
print('\n\t\t\t' + guest_list[3].upper() + message)
print('\n\t\t' + guest_list[4].title() + message)
print('\n\t' + guest_list[5].title() + message)
print('\n' + guest_list[6].title() + message)

print('\nOh no, our table got cancelled. Only two people will be invited now.')
message2 = "I'm so sorry, you didn't make the cut, "

print(message2 + guest_list.pop() + '.')
print(message2 + guest_list.pop() + '.')
print(message2 + guest_list.pop() + '.')
print(message2 + guest_list.pop() + '.')
print(message2 + guest_list.pop() + '.')

print(guest_list[0].title() + ', you are still invited!')
print(guest_list[1].title() + ', you are still invited!')

del guest_list[0]
del guest_list[0]

print(guest_list)