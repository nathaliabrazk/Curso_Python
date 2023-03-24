#LIST
#Program will read several numbers and put on a list, before this show: 
#A) how many numbers were typed B) The list of values order in decreasing order
#C) if the value 5 was typed and if him is on list or not 
n = list()
op = ''
quant = 0
while True:
    n.append(int(input('Type a number:')))
    quant += 1
    op = str(input('Continue?')).strip().upper()
    if op == 'NO':
        break
    if op not in 'YESNO':
        op = str(input('Type just yes or no, continue?')).strip().upper()
n.sort(reverse = True)
print('=' * 30)
print('             INFO')
print('=' * 30)
print(f'Amount of values entered:{quant}')
print(f'List: {n}')
if 5 in n:
    print('The value 5 is on list!')
else:
    print('The value 5 is not on list!')

    