#Program who read a real number and show your whole portion
import math
n = float(input( 'Type a real number:' ))
w = math.trunc(n) 
print( 'The wole portion to: {} is: {}'.format(n,w) )