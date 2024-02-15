#return functions

def city_country(city, country):
    formatted = city + ', ' + country
    return formatted.title()

answer = city_country('dallas', 'usa')
print(answer)