#Program where the user can type some numerical values and register them. If the number already
#exist in there, him dont gonna be register. On the end show all the register values on ascending order
register = []
op = ''
register.append(float(input('Type a value:')))
op = str(input('Do you want continue?'))
while op != 'NOno':
    register.append(float(input('Type a value:')))
    if register != register:
        print('Value register with sucess!')
    else:
        register.remove(register)
        print('Duplicade value i cant register!')
        op = str(input('Do you want continue?'))
        if op == 'NOno':
            break
print('=' * 25)
print(f'{"REGISTER VALUES"}'^25)
print('=' * 25)
print(f'{register.sort()}')