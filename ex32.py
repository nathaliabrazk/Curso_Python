#Program will read a any year and show if he is bissextile
from datetime import date
year = int(input('Type the year you want to analyze(if you want to analyze the current year type 0):'))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('The year {} is BISSEXTILE!'.format(year))
else:
    print('The year {} is NOT bissextile!')