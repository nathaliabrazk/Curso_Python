#Program who reed two numbers and show the menu:
#[1] add
#[2] multiply
#[3] bigger
#[4] type new numbers 
#[5] go out the program
#Your program need perform the requeseted operation
n1 = int(input('Type the first number:'))
n2 = int(input('Type the second number:'))
print('=' * 28)
print('            MENU')
print('=' * 28)
print('    [1] Add\n    [2] Multiply\n    [3] Bigger\n    [4] Type new numbers\n    [5] Go out the program')
op = int(input('Type your choice:'))
if op == 1:
    print('You choice add!')
    add = n1 + n2
    print('The sum of {} and {} are: {}'.format(n1,n2,add))