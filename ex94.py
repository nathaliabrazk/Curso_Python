#DICIONARY
#LIST OF DICIONARYS
#The program will read the name, age, sex of a several people keeping the datas of each person on a dicionary
#and all the dicionarys on a list. Show:
#a)How much people were registered *
#b)The avarage of age from the group 
#c)A list with all the womans*
#d)A list with all the people with age above average 
data = dict()
allpeople = list()
op = ''
while True: 
    allpeople.clear()
    data['name'] = str(input('Name: '))
    while True:
        data['sex'] = str(input('Sex [F/M]')).strip().upper()
        if data['sex'] in 'FM':
            break
        print('ERROR! Type just [F/M]')
    data['age'] = int(input('Age: '))
    allpeople.append(data.copy())
    while True:
        op = str(input('Continue? ')).upper()[0]
        if op in 'YESNO':
            break 
        print('ERROR! Type just yes or no')
        if op == 'NO':
            break 
    print('-=')
    print(allpeople)
