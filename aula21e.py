#FUNCTIONS PT 2
#Scope of variables 

#function
def test(b):
    global a #Global variable being used inside the function
    a = 8 #Other variable with name a but local, not global 
    b += 4
    c = 2
    print(f'a inside equals to {a}')#Local variable
    print(f'b inside equals to {b}')#Local variable
    print(f'c inside equals to {c}')#Local variable
#main

a = 5#Global variable 
test(a)
print(f'a outsize equals to {a}')#Global variable 
print(f'b outsize equals to {b}')#Local variable
print(f'c outsize equals to {c}')#Local variable