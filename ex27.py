#Program will read a full name of a people, showing next the first and last name separately
name = str(input('Type a full name:')).strip()
b = name.split()
print('The first name is:{}'.format(b[0]))
print('The last name is:{}'.format(b[len(b)-1]))