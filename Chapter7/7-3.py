multiples = input('Provide a number and I will tell you if it is a multiple of 10. ')
multiples = int(multiples)

if multiples % 10 == 0:
    print('Yes, ' + str(multiples) + ' is a multiple of 10!')
else:
    print('No, ' + str(multiples) + ' is not a multiple of 10.')