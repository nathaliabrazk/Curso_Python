#Program will read the age and sex of several people. For each register person, the program will go ask for 
#the user if he wants continue. At the end show: a) How many people is over 18 years old b) How many mans
#were registered c)How many womens are under 20 years old 
over18 = 0
man = 0
women = 0 
op = ''
age = int(input('Type the age:'))
sex = str(input('Type the sex[F/M]:')).strip().upper()
while op != 'NO':
    op = str(input('Continue? ')).strip().upper()
    if op == 'YES':
        age = int(input('Type the age:'))
        sex = str(input('Type the sex[F/M]:')).strip().upper()
        if age < 18:
            over18 += 1
        if sex == 'F' and age < 20:
            women += 1
        elif sex == 'M':
            man += 1
        if op == 'NO':
            break
    print('end')
    print(f'People over 18 = {over18}')
    print(f'Man registered = {man}')
    print(f'Women under 20 = {women}')

        
          
