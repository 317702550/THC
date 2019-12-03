#!/usr/bin/python3
# Maximiliano Proaño Bernal
# 03/12/19
# Python 3.7.3
# Año bisiesto

def is_leap(year):
    leap = False
    if year//4 != year/4:
        return(leap)
    elif year//100 == year/100:
        if year//400 == year/400:
            return(not leap)
        else:
            return(leap)
    else:
        return(not leap)
year = int(input())
