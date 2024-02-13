# Donovan McKinney
# Python
# Mod 4 Lab 1 
# 2/13/2024 

from helper import get_int

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}({self.age})"
        

p1 = Person(input("\nEnter your name: "), get_int("Enter the age of the person: "))
p2 = Person(input("\nEnter your name: "), get_int("Enter the age of the person: "))
p3 = Person(input("\nEnter your name: "), get_int("Enter the age of the person: "))

print (p1)
print (p2)
print (p3)

#I was there