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
regist['name'] = str(input('Name:'))
yob = int(input('Year of birth:'))
age = ActualYear - yob#variable who make the calculation for get the actual year
regist['age'] = age
regist['work'] = str(input('Work card:'))
print(age)

