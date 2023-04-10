#FUNCTIONS PT 2
#Scope of variables 

#This program dont gonna work because x be declared just on function, already n be declared on global form
#function
def test():
    x = 8
    print(f'On function test, n equals to {n}')
    print(f'On function test, x equals to {x}')

#main
n = 2#Global variable 
print(f'On main, n equals to {n}')
print(f'On main, x equals to {x}')
test()