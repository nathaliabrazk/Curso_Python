#program who convert a typed temperature to °C and convert to °F
c = int(input( 'Type a temperature in °C:' ))
f = c * 1.8 + 32
print( 'The temperature {}°C equals {:.1f}°F'.format(c,f) )