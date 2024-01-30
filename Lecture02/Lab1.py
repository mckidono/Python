# Donovan McKinney
# Python
# Mod 2 Lab 1 
# 1/31/2024


print("This program will calculate the area")
#length=float( input("Input a number: "))
#width=float( input("Input a second number: "))

def get_area(length, width):
    #Accepts two parameters
    #Returns the area by multiply the two parameters
    #length=float( input("Input a number: "))
    #width=float( input("Input a second number: "))
    return length * width
    
def calculate_area_from_user():
    #Accepts no parameters
    #Gets two float inputs from the user
    #Calculates the area using the previous function
    #Prints the result rounded to the hundredths place
    length=float( input("Input a number: "))
    width=float( input("Input a second number: "))
    area = round( get_area(length, width), 2)
    print("Area: " + str(area))
    
x=0    
while x != 3:
    calculate_area_from_user()
    x += 1