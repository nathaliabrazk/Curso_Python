#Program will read a full name and show: 
# *The name in all uppercase letters;
# *The name in all lowercase letters; 
# *Number of letters not counting spaces (using split).
name = str(input('Type a full name:')).strip()
print('The name in uppercase:', name.upper())
print('The name in lowercase:', name.lower())
print('The name has:',len(name),'letters')
print('The first name has: ', 'letters')
b = name.split()
print('Your first name is: {} and he has: {} letters'.format(b[0], len(b[0])))