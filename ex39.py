#Program will read the year of birth of a young and inform, according with your age:
#If him still goin to enlist, if its the time of enlist, if passed the time of the enlist
#(The program should show the time left or thath passed of the deadline)
from datetime import date
print('-*' * 20) 
print('            Military enlistment')
print('-*' * 20)
birth = int(input('Type the birth year: '))
today = date.today().year
year = today - birth
miss = 18 - year
delay = year - 18
print('You have {} years'.format(year))
if year < 18:
    print('You still goin to enlist!')
    print('You must enlist in {} years!'.format(miss))
elif year == 18:
    print('You must enlist this year!')
    print('Good luck!')
else:
    print('You should have enlisted by now!')
    print('Its {} years late!'.format(delay))