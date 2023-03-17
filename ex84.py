#Program who read the name and weight from a lot of people keeping the information on a list. At the end show
#A)How many people were registered. b)A list with the heavier people. c)A list with the more skinny people
temporary = []
principal = []
big = 0
small = 0
while True:
    temporary.append(str(input('name:')))#gonna be registered in position 0
    temporary.append(float(input('weight:')))#gonna be registered in position 1
    if len(principal) == 0:
        big = smal = temporary[1]
    else:
        if temporary[1] > big:
            big = temporary[1]
        if temporary[1] < small:
            small = temporary[1]
    principal.append(temporary[:])#[:] is for copy all the respository
    temporary.clear()#clear() its for init a list when the loop finish
    op = str(input('Continue?')).strip().upper()
    if op in 'NO':
        break
print('-' * 30)
print('            RESULT' )
print('-' * 30)
print('Typed datas: ',principal)
print('Total of people: ',len(principal))
print(f'The biggest weight was : {big} kg from: ',end='')
for p in principal:#loop for show the name of people
    if p[1] == big:
        print(f'[{p[0]}]')
print('')
print(f'The smallest weight was : {small} kg from: ',end='')
for p in principal:#loop for show the name of people
    if p[1] == small:
        print(f'[{p[0]}]')
print('')
