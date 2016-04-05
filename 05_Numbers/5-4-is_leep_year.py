#!/usr/bin/env python
def is_leep_year(year):
    if year % 4 == 0:
        if year % 100 != 0 :
            return True
        elif year % 400 == 0:
            return True
        else:
            return False
    else:
        return False

print is_leep_year(1992)
print is_leep_year(2000)
print is_leep_year(1900)
print is_leep_year(1999)