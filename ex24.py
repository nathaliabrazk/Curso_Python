#Program will read a city's name and say if it starts with "Santo"
city = str(input('Type city name:')).strip()
print(city[:5].upper() == 'SANTO')
