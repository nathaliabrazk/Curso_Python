#Program who reed two numbers and show the menu:
#[1] add
#[2] multiply
#[3] bigger
#[4] type new numbers 
#[5] go out the program
#Your program need perform the requeseted operation
n1 = int(input('Type the first number:'))
n2 = int(input('Type the second number:'))
op = 0
while op != 5:
    print('=' * 28)
    print('            MENU')
    print('=' * 28)
    print('    [1] Add\n    [2] Multiply\n    [3] Bigger\n    [4] Type new numbers\n    [5] Go out the program')
    op = int(input('Type your choice:'))
#add
    if op == 1:
        print('You choice add!')
        add = n1 + n2
        print('The sum of {} and {} are: {}'.format(n1,n2,add))
#multiply
    elif op == 2:
        print('You choice multiply!')
        mult = n1 * n2
        print('The multiply of {} and {} are: {}!'.format(n1,n2,mult))
#bigger
    elif op == 3:
        print('You choice bigger!')
        if n1 > n2:
            print('The number {} is greater than {}!'.format(n1,n2))
        elif n2 > n1:
            print('The number {} is greater than {}!'.format(n2,n1))
        elif n1 == n2:
            print('The numbers are the same!')
#Type new numbers
    elif op == 4:
        print('You choice type new numbers!')
        n1 = int(input('Type the first number:'))
        n2 = int(input('Type the second number:'))
        
print('End of the program\nThank you for your visit and see you soon!')