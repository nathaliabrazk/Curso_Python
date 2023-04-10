#FUNCTION PT 2
#Program who has a function calling vote() who recives the year of birth like parameter, returning 
#the literal value indicating if the person has the vote DENIED, OPTIONAL or MANDATORY on elections
#function
def vote(year):
    from datetime import date#local import
    actual = date.today().year
    age = actual - year
    if age < 16:
        return f'With {age} years: DENIED'
    elif age < 18 and age >= 16:
        return f'With {age} years: OPTIONAL'
    elif age > 18:
        return f'With {age} years: MANDATORY'
birth = int(input('Type the year of your birth: '))
print(vote(birth))