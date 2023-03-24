#Program will read a full name and show: 
# *The name in all uppercase letters; 
# *The name in all lowercase letters;
# *Number of letters not counting spaces.
name = str(input('Type a full name:')).strip()
print('Name in all uppercase letters: ', name.upper())
print('Name in all lowercase letters:', name.lower())
print('Name has: {} letters'.format(len(name) - name.count(' ')))
print('Name has: {} letters'.format(name.find(' ')))