#DICIONARY
#LIST OF DICIONARYS
#The program will read the name, age, sex of a several people keeping the datas of each person on a dicionary
#and all the dicionarys on a list. Show:
#a)How much people were registered *
#b)The avarage of age from the group 
#c)A list with all the womans*
#d)A list with all the people with age above average 
allPeople = list()
people = dict()
sum = average = 0
people['name'] = str(input('Name: '))
while True:
    people['sex'] = str(input('Sex [F/M]: ')).upper()[0]#[0] to get just the first letter
    if people['sex'] in 'MF':
        break
    print('ERROR - Type just [F or M]')