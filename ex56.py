#Program who read the name, age and sex from 4 people. In the end show: the average of age from the group
#What's the name of the oldest man. How many women are under 20. 
print('-' * 10) 
print('   FORM')
print('-' * 10)
sumage = 0
average = 0
oldestman = 0
nameman = ''
womenunder = 0
for c in range (1,5):
    print('-----{}ª Person-----'.format(c))
    name = str(input('Name:')).strip()
    age = int(input('Age:'))
    sex = str(input('Sex [M/F]:')).strip().upper()
    sumage += age 
    average = sumage / 4
    if c == 1 and sex in 'M':
        oldestman = age
        nameman = name
    if sex in 'M' and age > oldestman:
        oldestman = age
        nameman = name
    if sex in 'F' and age < 20:
        womenunder += 1

print('The avarage of age from the group: {}'.format(average))
print('The oldest man name is: {} with {} years old!'.format(nameman, oldestman))
print('The quantidy of womens under 20 years old: {}'.format(womenunder))
