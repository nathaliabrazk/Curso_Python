#Program who read the name, age and sex from 4 people. In the end show: the average of age from the group
#What's the name of the oldest man. How many women are under 20. 
print('-' * 10) 
print('   FORM')
print('-' * 10)
for c in range (1,5):
    name = str(input('{}° name:'.format(c))).strip()
    age = int(input(('{}° age:'.format(c))))
    sex = str(input('{}° sex:'.format(c))).strip().upper()
    
average = sex / 4
    
print('The avarage of age from the group: {}'.format(average))
