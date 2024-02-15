pokemon1 = '\tcharmander   '
pokemon2 = '\n\n     squirtle'

print(pokemon1)
print(pokemon2)

print(pokemon1.strip())
print(pokemon2.lstrip())

print(pokemon1.rstrip())


#you can pass other variables or parameters within the strip function as well

pokemon3 = 'pppppbulbasaurppppp'
thing = 'p'

print(pokemon3)
print(pokemon3.lstrip('p'))
print(pokemon3.strip(thing))