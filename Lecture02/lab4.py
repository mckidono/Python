# Donovan McKinney
# Python
# Mod 2 Lab 4 
# 1/31/2024
import datetime

def get_birthdate():
    year=int(input("What year were you born: "))
    month=int(input("What month were you born: "))
    day=int(input("What date were you born: "))
    dob = datetime.date(year, month, day)
    return dob 

def get_age(date):
    today = datetime.date.today()
    age = today.year - date.year
    if today.month < date.month or (today.month == date.month and today.day < date.day):
        age -= 1
    return age


date = get_birthdate()
age = get_age(date)
print("Your age is:", age)

if age >= 16:
    print("You can drive")
    
if age >= 18:
    print("You can vote")
 
is_qualified = False
    
if age >= 35:
    Born_Cit = input("Are you a natural born citizen (y/n): ")
    if Born_Cit == 'y' or Born_Cit == 'Y':
        if input("Have you lived in the us for 14 years (y/n): ") == 'y':
            is_qualified = True
            
if is_qualified:
    print("You can become president")
else:
    print("You cannot become the president")
        