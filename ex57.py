#Program who read the sex of a person, but just acept the values 'M' or 'F'. In case of error ask for 
#typing again until you have the correct reply
sex = str(input('Type the sex [F/M]:')).strip().upper()[0]
while sex not in 'FfMm':
    sex = str(input('Invalid (Just type [F or M]):')).strip().upper()[0]
