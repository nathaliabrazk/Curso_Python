#DICIONARY
#The program will read the name, age, sex of a several people keeping the datas of each person on a dicionary
#and all the dicionarys on a list. Show:
#a)How much people were registered *
#b)The avarage of age from the group 
#c)A list with all the womans
#d)A list with all the people with age above average 
data = dict()
op = ''
woman = list()
quant = 0
avarage = 0
while True:
    data['name'] = str(input('Name: '))
    data['age'] = int(input('Age: '))
    data['sex'] = str(input('Sex [F/M]: '))
    quant += 1
    if data['sex'] not in 'FM':
        data['sex'] = str(input('Type just F or M: '))
    if data['sex'] in 'F':
        woman.append(data)
    op = str(input('continue? ')).strip().upper()
    if op in 'NOno':
        break
avarage = sum(data['age']) / quant
print('-=' * 30)
print(f'Quantidy of people registered: {quant}')
print(f'The avarage of age from the people: {avarage}')
print(f'List with the womans:\n{woman}')
#print(f'List of people with age above average:\n{}')