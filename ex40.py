#Program will read two notes and calculate your average, showing a massage at the and
#according to the average reached(average bellow of 5,0-disapproved, average between 5.0 and 6.9- recovery
#average 7.0 or higher - approved)
note1 = int(input('Type the first note:'))
note2 = int(input('Type the second note:'))
average = (note1 + note2) / 2
if average < 5.0:
    print('Your average is:{}'.format(average))
    print('You are DISAPPROVED!')
elif  average >= 5.0 and average <= 6.9:
    print('Your avarage is:{}'.format(average))
    print('You are on RECOVERY!')
