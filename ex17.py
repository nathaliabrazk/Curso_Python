#Program who reed the length of a opposite cathetus and adjacent cathetus of a right triangle, calculate and show the length of the hypotenuse
import math
o = int(input( 'Type the opposite cathetus:' ))
a = int(input( 'Type the adjacent cathetus:' ))
l = math.hypot(o,a)
print( 'The lenght of the hypotenuse is:{}'.format(l))
