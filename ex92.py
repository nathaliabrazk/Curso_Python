#DICIONARY
#Program will read name, year of birth and work card and regist them(with age) on a dicionary. If
#the CTPS is different of 0 the dicionary receive too the hiring year and the salary. Calculate 
#and add, in addition the age, with how many years the people gonna retire(the people gonna retire before 35
#years of colaboration)
#library to most the actual year
import datetime
date = 0
regist = dict()#dicionary
yob = 0#variable to regist the year of birth to the user
ActualYear = 2022#variable to regist the actual year
RetireYear = 0#variable to calculate with how many years the user gonna retire
regist['name'] = str(input('Name:'))
yob = int(input('Year of birth:'))
age = ActualYear - yob#variable who make the calculation for get the actual year
regist['age'] = age
regist['work'] = str(input('Work card:'))
if regist['work'] != 0:
    regist['hiring'] = int(input('Hiring year:'))
    regist['salary'] = float(input('Salary:'))
elif regist['work'] == 0:
    print('You need be in a work!')
print('-=' * 30)
print(f'{"name"} gonna retire with {RetireYear} years')

   


