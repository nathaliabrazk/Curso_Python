#COMPOSITE VARIABLES
#Program will have a tuple tottaly completed with a count by extension, from 0 until 20 
#The program must read one number (between 0 and 20 ) and show he by extensive
count = ('Zero', 'One', 'Two', 'Three', 'Four',
          'Five', 'Six', 'Seven', 'Eight',
            'Nine', 'Ten', 'Eleven', 'Twelve',
              'Thirteen', 'Fourteen', 'Fivteen', 'Sixteen',
                'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')
extense = ''
while True:
    number = int(input('Type a number (between 0 and 20): '))
    if number > 20 or number < 0:
        number = int(input('Invalid!(Type just numbers between 0 and 20)\nTry again:'))
    if number == 0:
        extense = count[0]
    elif number == 1:
        extense = count[1]
    elif number == 2:
        extense = count[2]
    elif number == 3:
        extense = count[3]
    elif number == 4:
        extense = count[4]
    elif number == 5:
        extense = count[5]
    elif number == 6:
        extense = count[6]
    elif number == 7:
        extense = count[7]
    elif number == 8:
        extense = count[8]
    elif number == 9:
        extense = count[9]
    elif number == 10:
        extense = count[10]
    elif number == 11:
        extense = count[11]
    elif number == 12:
        extense == count[12]
    elif number == 13:
        extense == count[13]
    elif number == 14:
        extense == count[14]
    elif number == 15:
        extense == count[15]
    elif number == 16:
        extense == count[16]
    elif number == 17:
        extense == count[17]
    elif number == 18:
        extense == count[18]
    elif number == 19:
        extense == count[19]
    elif number == 20:
        extense == count[20]
    print(f'You type the number: {extense}')