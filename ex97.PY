#FUNCTION
#Program who has a function called type(), who receive any text as parameter and show a message 
#with adaptable size
def type(message):
    size = len(message) + 4
    print('~' * size)#This gonna serve to the edge be adaptable to te text
    print(f'  {message}')
    print('~' * size)

text = str(input('Type the text: '))
type(text)