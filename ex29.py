#CONDITIONAL
#Program will read a car speed, if the car exceed 80 km\h show an message sayng "You was fined". 
# The fine it will coast R$ 7,00 for every km over the limit
v = int(input('Type the car speed in km\h:'))
if (v - 80) > 80:
    print('YOU WAS FINED for exceeding the speed limit of 80km/h!')
    print('The speeding ticket value: R$ {}'.format(v * 7))
else:
    print('Have a good day, drive with security!')
