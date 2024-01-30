# Donovan McKinney
# Python
# Mod 2 Lab 3
# 1/31/2024

def get_generation():
    year = int(input("What year were you born?: "))
    if year >= 2013:
        return 'Alpha'
    elif year >= 1997:
        return 'Gen Z'
    elif year >= 1981:
        return 'Millennial'
    elif year >= 1965:
        return 'Gen X'
    elif year >= 1946:
        return 'Baby Boomer'
    else:
        return 'Wow!'
    
x=0
while x < 3:
    print(get_generation())
    x += 1