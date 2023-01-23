#program who read the width and the heigh of a wall in meters, calculate your area and the amount of tint necessary to paint there, knowing that eacher liter, paint an area 2m2
width = int(input( 'Type the whidth:' ))
height = int(input( 'Type the height:' ))
area = width*height
tint = area/2
print('Go be necessary {} liters of tint'.format(tint))