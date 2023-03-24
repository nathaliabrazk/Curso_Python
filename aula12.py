#CONDITIONAL
#nested conditions
name = str(input('Type your name:'))
if name == 'Fulano':
    print('What beautiful name {}!'.format(name))
elif name == 'Maria' or name == 'Pedro':
    print('Your name is popular!')
else:
    print('Your name is normal!\nHave a good day {}'.format(name))