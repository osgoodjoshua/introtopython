#Every function challenge

pokemons = ['charmander', 'bulbasaur', 'squirtle', 'pikachu']
print(pokemons)
print(len(pokemons))

pokemons.append('mewtwo')
print(pokemons)

pokemons.insert(3, 'golem')
print(pokemons)

print(sorted(pokemons))
print(sorted(pokemons, reverse=True))
print(pokemons)

print('The pokemon ' + str(pokemons.pop()) + ' has been removed.')
print(pokemons)

grassType = 'bulbasaur'
pokemons.remove(grassType)
print('All grass-type pokemon have been removed.')
print(pokemons)

pokemons.sort()
print(pokemons)
pokemons.sort(reverse=True)
print(pokemons)

pokemons.reverse()
print(pokemons)
pokemons.reverse()
print(pokemons)

print('You have ' + str(len(pokemons)) + ' pokemons remaining.')

del pokemons[0]
del pokemons[0]
del pokemons[0]

print('You now have ' + str(len(pokemons)) + ' pokemon remaining.')

print(str(pokemons[0]).title() + ' is your only pokemon left! 🔥')





