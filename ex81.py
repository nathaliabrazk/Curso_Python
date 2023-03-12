#Program will read several numbers and put on a list, before this show: 
#A) how many numbers were typed B) The list of values order in decreasing order
#C) if the value 5 was typed and if him is on list or not 
n = list()
op = ''
quant = 0
five = False
p = ''
while True:
    n.append(int(input('Type a number:')))
    quant += 1
    op = str(input('Continue?')).strip().upper()
    if op == 'NO':
        break
    if 5 in n:
        five == True
        if five == True:
            p = 'YES'
    else:
        p == 'NO'
n.sort(reverse = True)
print('             INFO')
print('=' * 30)
print(f'Amount of values entered:{quant}')
print(f'List\n{n}')
print(f'Number 5 is on list? {p}')

    