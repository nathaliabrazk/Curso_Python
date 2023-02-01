#Program will read a full name and show: the name in all capital letters , the name in all lowercase letters, 
#number of letters not counting spaces
name = str(input('Type a full name:')).strip()
print('Name in all uppercase letters: ', name.upper())
print('Name in all lowercase letters:', name.lower())
print('Name has:', len(name) - name.count(' '), 'letters')
print('The first name has', name.find(' '), 'letters')