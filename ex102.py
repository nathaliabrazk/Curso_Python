#FUNCTION PT 2
#Program who has a function calling factorial() who recives two parameters: the first who indicate  the number
#to calculate and other calling show, who gonna be optional who indicate if be showed or not on the screen
#the process of factorial calculation

#Function
def factorial(n, show=False):
    """
    Calculate the factorial of a number
    :n: The number
    :show: logical variable who show on the screen the factorial if be True
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} x ', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#main
print(factorial(5, show=True))
help(factorial)