#Program who read the age of 7 people and show how many people have not yet reached the age of majority
from datetime import date
actual = date.today().year
minor = 0
lage = 0
for c in range (1,8):
    year = int(input('Type you year of birth:'))
    if actual - year < 18:
        minor += 1 
    else:
        lage += 1
print('Quantidy of people who reached the age of majority: {}'.format(lage))
print('Quantidy of people who have not reached the age of majority: {}'.format(minor))