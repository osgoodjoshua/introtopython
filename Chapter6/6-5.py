rivers = {
    'nile' : 'egypt',
    'mississippi' : 'north america',
    'amazon' : 'south america'
    }

for river in rivers:
    print('The ' + river.title() + 
          ' river is located in ' + 
          rivers[river].title() + '.')
    
for i in rivers.keys():
    print(i)

for j in rivers.values():
    print(j)
