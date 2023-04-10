#FUNCTION
#Program who has a function calling bigger(), who receive several intenger values. The program will analize 
#all the values and say wich one is bigger

#function
def bigger(* values):
    count = bigger = 0
    print('Analizing the past values...')
    for number in values:
        print(f'{number} ', end='')

#main
bigger()
bigger()
bigger()
bigger = int(input('Type several values to know wich one is bigger: '))


