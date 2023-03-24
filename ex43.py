#METHODS
#Develop a logic that reads a person's weight and height, calculates his BMI and shows his status according
#to the table: |bellow of 18.5 = bellow of weight| |between 18.5 and 25 = ideal weight| |25 to 30 = overweight|
#|30 to 40 = obesity| over 40 = morbid obesidy 
weight = float(input('Type the weight:'))
height = float(input('Type your height:'))
bmi = weight / (height * 2)
print('Your BMI is:{}'.format(bmi))
if bmi < 18.5:
    print('You are bellow of weight!')
elif bmi >=18.5 and bmi < 25:
    print('You are on ideal weight!')
elif bmi >= 25 and bmi < 30:
    print('You are overweight!')
elif bmi >= 30 and bmi <= 40:
    print('You are on obesity!')
elif bmi > 40:
    print('You are on morbid obesity!')