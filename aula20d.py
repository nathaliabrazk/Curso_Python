#FUNCTIONS
def sum(* values):
    s = 0
    for number in values:
        s += number
    print(f'Adding the values {values} we have {s}') 
sum(5, 2)
sum(2, 9, 4)
