#Program will read one name and two notes from several students and regist all in a compound list. 
#At the end, it shows a bulletin with the average of each one and allows the user to show the grade 
#of each student individually
note = []
name = str(input('Name:'))
for c in range(0,2):
    note = int(input(f'{c} Note:'))
print(f'Name: {name}')
print(f'Note: {note}')