#Program will read a whole number and ask the user to choose which will be the base for the conversion
#1 to the binary, 2 to octal and 3 to hexadecimal 
number = int(input('Type a number:'))
print('Choose a conversion base:')
choice = int(input('|1| Convert to binary\n|2| Convert to octal\n|3| Convert to hexadecimal\nType your choice:'))
if choice == 1:
    print('The number {} in binary is: {}'.format(number,bin(number)[2:]))
elif choice == 2:
    print('The number {} in binary is: {}'.format(number, oct(number)[2:]))
elif choice == 3:
    print('The number {} in hexadecimal is: {}'.format(number,hex(number)[2:]))
else:
    print('Invalid!(type 1, 2 or 3)')
