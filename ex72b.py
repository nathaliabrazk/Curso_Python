#Program will have a tuple tottaly completed with a count by extension, from 0 until 20 
#The program must read one number (between 0 and 20 ) and show he by extensive
count = ('Zero', 'One', 'Two', 'Three', 'Four',
          'Five', 'Six', 'Seven', 'Eight',
            'Nine', 'Ten', 'Eleven', 'Twelve',
              'Thirteen', 'Fourteen', 'Fivteen', 'Sixteen',
                'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')
while True:
    number = int(input('Type a number between 0 and 20: '))
    if 0 <= number <= 20:
        break
    print('Try again.', end='')
print(f'You type a number {count[number]}')