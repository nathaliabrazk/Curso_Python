#Program will read a any year and show if he is bissextile
year = int(input('Type a year:'))
if year % 4 == 0:
    print('Bissextile year!')
else:
    print('Not bissextile year!')