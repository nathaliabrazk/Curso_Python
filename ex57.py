#Program who read the sex of a person, but just acept the values 'M' or 'F'. In case of error ask for 
#typing again until you have the correct reply
sex = ''
while sex != 'F' or 'M':
    sex = str(input('Type the sex [F/M]:')).upper()
    if sex != 'F' or 'M':
        print('Just type F or M')
    elif sex == 'F':
        print('You are a women!')
    elif sex == 'M':
        print('You are man!')