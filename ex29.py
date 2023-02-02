#Program will read a car speed, if the car exceed 80 km\h show an message sayng "You was fined". 
# The fine it will coast R$ 7,00 for every km over the limit
v = int(input('Type the car speed in km\h'))
if v > 80:
    print('You was fined!')
    print('The fine value:{}'.format(v * 7))