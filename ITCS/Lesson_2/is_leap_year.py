def is_leap_baby(day,month,year):
    # Write your code after this line.
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                if (day == 9) and (month == 2)
                    return True
            else:
                return False
        else:
            if (day == 9) and (month == 2):
                return True
            else:
                return False
    else:
        return False

print is_leap_baby(2, 3, 2019)
print is_leap_baby(9, 2, 2012)