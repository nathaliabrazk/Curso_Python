#Program will read several numbers and put them in a list, after that it will make 2 extra lists that will have
#only even values and odd values respectively. At the end show the content of the 3 lists
number = list()
pair = list()
odd = list()
while True:
    number.append(int(input('Type the number:')))
    op = str(input('Continue?')).strip().upper()
    if op in 'NOno':
        break
    elif op not in 'YESyesNOno':
        op = str(input('Type just yes or no!\nContinue?'))
for i, v in enumerate(number):
    if v % 2 == 0:
        pair.append(v)
    elif v % 2 == 1:
        odd.append(v)
print('=' * 25)
print('LISTS')
print('=' * 25)
print(f'Original list: {number}')
print(f'Even list: {pair}')
print(f'Odd list: {odd}')