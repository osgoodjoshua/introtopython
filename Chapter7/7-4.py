pizzatoppings = 'What topping would you like to add to your pizza? '
pizzatoppings += "Enter 'quit' when you are finished. "

message = ""

while message != 'exit':
    message = input(pizzatoppings)
    if message != 'exit':
        print(message + ' has been added to your pizza.')