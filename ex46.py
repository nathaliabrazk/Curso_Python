#Program who read show in the screen the countdown to the burst of fireworks goin from 10 to 0
#with a break of 1 second between they 
from time import sleep
for count in range(10, 0-1, -1):
    print(count)
    sleep(0.5)
print('BOOM!')