pokemons = ['bulba', 'char', 'pika', 'squirtle', 'golem', 'mew']

print('The first three items in this list are:')
for pokemon in pokemons[:3]:
    print(pokemon)

print('The items in the middle of the list are:')
for pokemon in pokemons[1:4]:
    print(pokemon.title())


print('The last three items in this list are:')
for pokemon in pokemons[-3:]:
    print(pokemon)

