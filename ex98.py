#FUNCTION
#Program who has a function called count(), who receive three parameter: Start, end, step. The program needs to do
#three counts
#a)From 1 until 10 from 1 in 1 
#b)From 10 until 0 from 2 in 2
#c)A custom count
from time import sleep 


#function
def counter(s, e, st):
    #Logic validation 
    if st < 0:
        st *= - 1
    if st == 0:
        print('This count dont be made, im gonna made from 1 in 1')
        st = 1
    print('-=' * 20)
    print(f'Count from {s} until {e} from {st} in {st}')
    sleep(2)
    if s < e:  
        count = s
        while count <= e:
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
            count += st
        print('end')
    else:
        count = s
        while count >= e:
            print(f'{count} ',end='', flush=True)
            sleep(0.5)
            count -= st
        print('end')
    print('-=' * 20)


#Main
counter(1, 10, 1)
counter(10, 0, 2)
print('Now its your time to personalize the count!')
start = int(input('Start:           '))
end = int(input('End:             '))
steps = int(input('How many steps?  '))
#Calling the function 
counter(start, end, steps)
