#program who read the width and the heigh of a wall in meters, calculate your area and the amount of tint necessary to paint there, knowing that eacher liter, paint an area 2m2
width = float(input( 'Type the whidth:' ))
height = float(input( 'Type the height:' ))
area = width*height
tint = area/2
print('Your wall have the dimension of {}x{}\nYour area is {}²\nYou will need {}l of tint'.format(width,height,area,tint))