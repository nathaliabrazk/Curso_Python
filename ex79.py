#Program where the user can type some numerical values and register them. If the number already
#exist in there, him dont gonna be register. On the end show all the register values on ascending order
register = []
op = ''
while True:
    register.append(float(input('Type a value:')))
    op = str(input('Do you want continue?')).strip().upper()
    while op == 'YESyes':
        register.append(float(input('Type a value:')))
        op = str(input('Do you want continue?')).strip().upper()
    if op == 'NOno':
            break
print('=' * 25)
print(f'{"REGISTER VALUES"}'^25)
print('=' * 25)
print(f'{register.sort()}')