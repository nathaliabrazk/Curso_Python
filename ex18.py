#Program who read any angle and show the sine value, cosine and tangent from this angle
import math 
a = int(input( 'Type a angle:' ))
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)
print( 'The sine of {0} is: {1}\nThe cosine of {0} is: {2}\nThe tangent of {0} is: {3}'.format(a,s,c,t))
