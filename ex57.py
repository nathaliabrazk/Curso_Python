#Program who read the sex of a person, but just acept the values 'M' or 'F'. In case of error ask for 
#typing again until you have the correct reply
sex = str(input('Type the sex (M or F): ')).upper().strip()[0]
while sex != 'F' and sex != 'M':
    sex = str(input('Invalid!. Type just (M or F):')).upper().strip()[0]
if sex == 'F':
    print('Female sex registered!.')
if sex == 'M':
    print('Masculine sex registered!')