#METHODS
#The national swimming confederation needs a program that reads the year of birth of an athlete 
#and shows your category, according to age: until 9 years old = Little | until 14 years old = Childish
#until 19 years old = Junior | until 20 years old = Sênior | Over 20 = Master
age = int(input('Type your age:'))
if age <= 9:
    print('You have {} years old, you are LITTLE!'.format(age))
elif age > 9 and age <= 14:
    print('You have {} yeras old, you are CHILDISH!'.format(age))
elif age <= 19:
    print('You have {} years old, you are JUNIOR!'.format(age))
elif age == 20:
    print('You have {} years old, you are SÊNIOR!'.format(age))
elif age > 20:
    print('You have {} years old, you are MASTER!'.format(age))
