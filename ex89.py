#Program will read one name and two notes from several students and regist all in a compound list. 
#At the end, it shows a bulletin with the average of each one and allows the user to show the grade 
#of each student individually
regist = list()
op = ''
while True:
    name = str(input('Name: '))
    note1 = float(input('1º note:'))
    note2 = float(input('2º note:'))
    average = (note1 + note2) / 2
    regist.append([name, [note1, note2], average])
    op = str(input('Continue?')).upper()
    if op == 'NO':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NAME":<10}{"AVERAGE":>8}')
print('-' * 26)
for i, a in enumerate(regist):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    query = int(input('You want see the notes of what student(999 stop the program): '))
    if query == 999:
        print('FINISHING...')
        break
    if query <= len(regist) - 1:
        print(f'Notes from {regist[query][0]} they are: {regist[query][1]}')
print('<<<END>>>')