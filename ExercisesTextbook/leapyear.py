#The general logic is to start narrow and grow broader in your conditions
#this format avoids complex nested if statements, allows clean logical structure
def isLeapYear(year):
    #all years divisible by 400 ARE leap years
    if year % 400 == 0:
        return True
    #years divisible by 100 (but NOT 400) are NOT leap years
    elif year % 100 == 0:
        return False
    #generally, the rest of years divisible by 4 (every 4 years-ish) ARE leap years
    elif year % 4 == 0:
        return True
    #and the rest are of course not leap years
    else:
        return False

assert isLeapYear(1999) == False
assert isLeapYear(2000) == True
assert isLeapYear(2001) == False
assert isLeapYear(2004) == True
assert isLeapYear(2100) == False
assert isLeapYear(2400) == True