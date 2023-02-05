#Remake the 35 ex about the triangles adding the resource to show what type of triangle go be formed
#equilateral = all the sides are the same | isoceles = two sides are the same  
# scalene = all the sides are different
a = int(input('Type the first straight line:'))
b = int(input('Type the second straight line:'))
c = int(input('Type the third straight line:'))
if a == b and b == c:
    print('The straights lines: {}, {} and {} form a equilateral triangle!'.format(a,b,c))
elif a == b and b != c:
    print('The straights lines:{}, {} and {} form a isoceles triangle!'.format(a,b,c))
elif a == c and c != b:
    print('The straights lines {}, {} and {} form a isoceles triangle!'.format(a,b,c))
elif c == b and b != a:
    print('The straights lines {}, {} and {} form a isoceles triangle!'.format(a,b,c))
elif a != b and b != c and c != a:
    print('The straights lines {}, {} and {}'.format(a,b,c))