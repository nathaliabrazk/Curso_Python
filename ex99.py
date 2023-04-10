#FUNCTION
#Program who has a function calling bigger(), who receive several intenger values. The program will analize 
#all the values and say wich one is bigger
from time import sleep


#function
def bigger(* values):
    count = bigger = 0
    print('Analizing the past values...')
    for number in values:
        print(f'{number} ', end='')
        sleep(0.3)
        if count == 0:
            bigger = number
        else:
            if number > bigger:
                bigger = number
        count += 1
    print(f'Were informed: {count} values.')
    print(f'The biggest value informed he was: {bigger}.')
#main
bigger(10, 5, 2, 60, 3, 1)


