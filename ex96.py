#FUNCTION
#Program that has a function calling area(), which receives the dimensions of a rectangular
#terrain (width and length) and show the area of the terrain

#Function
def area(width, lenght):
    a = width * lenght
    print(f'The area from a terrain {width} x {lenght} is: {a}m².')

#Main
print('TERRAIN CONTROL')
print('_' * 20)
w = float(input('Widht: '))
l = float(input('Lenght: '))
area(w, l)
