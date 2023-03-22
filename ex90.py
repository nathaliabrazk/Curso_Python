#DICIONARY
#Program will read a name and average from a student keeping too the situation on a dicionary. At the end show
#the content from the structure on the screen
student = dict()
student['Name'] = str(input('Name: '))
student['Avarage'] = float(input(f'average from {student["Name"]}: '))
if student['Avarage'] >= 7:
    student['Situation'] = 'Aproved!'
elif 5 <= student['Avarage'] < 7:
    student['Situation'] = 'Recovery!'
else:
    student['Situation'] = 'Desaproved!'
print('-=' * 30)
for k, v in student.items():
    print(f'{k} its equal to {v}')