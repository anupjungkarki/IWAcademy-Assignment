# Write an if statement to determine whether a variable holding a year is a leap year.
def checkLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = 2020
if checkLeapYear(year):
    print("Leap Year")
else:
    print("Not a Leap Year")
