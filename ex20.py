#A teatcher want to raffle the order of presentation of works from the students. Make a program who read the names of the four students and show the order drawn
import random
n1 = str(input( 'Write the first name:'))
n2 = str(input( 'Write the second name:'))
n3 = str(input( 'Write the third name:' ))
n4 =  str(input( 'Write the fourth name:'))
list = [n1,n2,n3,n4]
random.shuffle(list)
print( 'Presentation order:\n',list )