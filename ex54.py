#Program who read the age of 7 people and show how many people have not yet reached the age of majority
minor = 0
major = 0
lage = 0
for c in range(1,8):
    age = int(input('Type your age:'))
    if age < 21:
        minor += 1
    else:
        lage += 1
print('{} people have not yet reached'.format(minor))