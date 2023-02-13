#Program who read the sex of a person, but just acept the values 'M' or 'F'. In case of error ask for 
#typing again until you have the correct reply
##ex = str(input('Type the sex [F/M]:')).strip().upper()
#while not sex == 'F' and not sex == 'M':
#sex = str(input('Invalid (Just type [F or M]):')).strip().upper()
#print('Sex {} registered with sucess!'.format(sex))
s = str(input('Por favor, digite o sexo (M ou F): ')).upper().strip()[0]
while s != 'F' and s != 'M':
    s = str(input('Dados inválidos. Por favor, digite o sexo (M ou F): ')
            ).upper().strip()[0]
if s == 'F':
    print('Sexo Feminino cadastrado.')
if s == 'M':
    print('Sexo Masculino cadastrado.')