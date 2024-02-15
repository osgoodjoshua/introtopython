# import new_car_info as nc

# newcar1 = nc.carinfo('toyota', 'tundra', color='black', engine='v6')
# newcar2 = nc.carinfo('honda', 'civic', color='white', engine='4cylinder', windowtint=True)

# print(newcar1)
# print(newcar2)

from new_car_info import carinfo as c

newcar1 = c('toyota', 'tundra', color='black', engine='v6')
newcar2 = c('honda', 'civic', color='white', engine='4cylinder', windowtint=True)

print(newcar1)
print(newcar2)