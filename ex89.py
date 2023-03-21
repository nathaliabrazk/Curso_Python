#Program will read one name and two notes from several students and regist all in a compound list. 
#At the end, it shows a bulletin with the average of each one and allows the user to show the grade 
#of each student individually
regist = list()

name = str(input('Name: '))
note1 = int(input('1º note:'))
note2 = int(input('2º note:'))
average = (note1 + note2) / 2
regist.append([name, [note1, note2], average])
print('-=' * 30)
print('No.      NAME        AVERAGE')
print(regist)
print('-' * 30)
