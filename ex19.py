#A teatcher wants to draw one of his four students to erase the blackboard. Make a program that helps the teacher, reading the students name and writing the name of the chosen one
import random
s1 = str(input( 'Write the first name:' )) 
s2 = str(input( 'Write the second name:' ))
s3 = str(input( 'Write the third name:' ))
s4 = str(input( 'Write the fourth name:' ))
print( 'The name drawn was:{}'.format(random.choice([s1,s2,s3,s4])))