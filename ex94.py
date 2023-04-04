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
while True:#This while True it suits to regist all datas from dictionaryes on a list
    people.clear()#to reset the list and add a new user
    people['name'] = str(input('Name: '))
    while True:
        #validation
        people['sex'] = str(input('Sex [F/M]: ')).strip().upper()[0]#[0] to get just the first letter
        if people['sex'] in 'MF':
            break
        print('ERROR - Type just [F or M]')
    people['age'] = int(input('Age: '))
    allPeople.append(people.copy())#to regist a copy from the dicionary on a list
    while True:
        op = str(input('Continue [Y/N]? ')).strip().upper()[0]# [0] to get just the first letter 
        if op in 'YN':
            break
        print('Type just [Y or N]')
    if op in 'N':
        break
print('-=' * 30)
print(f'Quanty of registered people: {len(allPeople)}')

