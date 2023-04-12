#FUNCTIONS PT 2
#Opcional parameters
def sum(a, b, c):#if the function be declared like this the code dont go work because the function need 3 values for parameter
    """
    -> Make the sum of 3 values and show the result 
    :a: First value
    :b: Second value
    :c: Third value
    """
    s = a + b + c
    print(f'The sum has resulted: {s}')

sum(3, 2, 5)
sum(8, 4)#this gonna be wrong

#Funcional form with opcional parameters
def sum(a, b, c = 0):# c is a opcional parameter
    s = a + b + c
    print(f'The sum has resulted: {s}')

sum(3, 2, 5)
sum(8, 4)

def sum(a = 0, b = 0, c = 0):# all the parameters are opcional 
    s = a + b + c
    print(f'The sum has resulted: {s}')

sum(3, 2, 5)
sum(8, 4)