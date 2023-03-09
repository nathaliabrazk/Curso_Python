#Program where the user can type some numerical values and register them. If the number already
#exist in there, him dont gonna be register. On the end show all the register values on ascending order
register = list()
n = 0
op = ''
while True:
    n = float(input('Type a value:'))
    if n not in register:
        register.append(n)
        print('Successful registration!')
    else:
        print('Repeated numbers cant be regsister!')
    op = str(input('Continue?')).upper()
    if op in 'NO':
        break
    if op not in 'YESyesNOno':
        op = str(input('Type just yes or no\nContinue?')).upper() 
print('=' * 25)
print(f'{"REGISTER VALUES":^25}')
print('=' * 25)
register.sort()
print(f'{register}')