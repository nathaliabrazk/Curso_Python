#DICIONARY
#Program will read name, year of birth and work card and regist them(with age) on a dicionary. If
#the CTPS is different of 0 the dicionary receive too the hiring year and the salary. Calculate 
#and add, in addition the age, with how many years the people gonna retire(the people gonna retire before 35
#years of colaboration)
#library to most the actual year
from datetime import datetime
data = dict()#dicionary
data['name'] = str(input('Name: '))
birth = int(input(f'Year of birth from {data["name"]}: '))
data['age'] = datetime.now().year - birth
data['workcard'] = int(input('Work card (if you dont have type 0): '))
if data['workcard'] != 0:
    data['hiringYear'] = int(input(f'Hiring year of contratation of {data["name"]}: '))
    data['retire'] = data['age'] + ((data['hiringYear'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in data.items():
    print(f'  - {k} has the value {v}')  