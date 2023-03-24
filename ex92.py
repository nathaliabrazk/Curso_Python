#DICIONARY
#Program will read name, year of birth and work card and regist them(with age) on a dicionary. If
#the CTPS is different of 0 the dicionary receive too the hiring year and the salary. Calculate 
#and add, in addition the age, with how many years the people gonna retire(the people gonna retire before 35
#years of colaboration)
#library to most the actual year
import datetime
regist = dict()#dicionary
yob = 0#variable to regist the year of birth to the user#variable to regist the actual year
RetireYear = 0#variable to calculate with how many years the user gonna retire
regist['name'] = str(input('Name:'))
yob = int(input('Year of birth:'))
age = 2023 - yob#variable who make the calculation for get the actual year
regist['age'] = age
regist['workcard'] = int(input('Work card(if you dont have type 0:'))
if regist['workcard'] != 0:
    regist['hiringyear'] = int(input('Hiring year:'))
    regist['salary'] = float(input('Salary:'))
else:
    print('You need be in a work!')
RetireYear = regist['hiringyear'] + 35
RetireYear - regist['age']
miss = regist['hiringyear'] - yob#how old the user has when he has hired
retireAge = miss + 35
print('-=' * 30)
print(f'{regist["name"]} can retire on the year = {RetireYear}')
print(f'With {retireAge} Years old')
if 2023 - RetireYear > 35:
    print('You can retire now!')
else:
    print('You cant retire!')
