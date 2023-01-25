#program that reads data from the keyboard and returns its primitive type and all possible information about it 
s = input('Type something: ')#s in thits case its a object
print( 'The primitive type is:',type(s) )#if primitive type isnt declared the program allways will return str
print( 'Its a number?', s.isnumeric() )
print( 'Its a letter?', s.isalpha() )
print( 'Its alphanumeric?', s.isalnum() )
print( 'Only spaces were entered?', s.isspace() )
print( 'Are upercase letters?', s.isupper() )
print( 'Are lowercase?', s.islower() )
print('Are capital(upercase and lowercase ?', s.istitle() )