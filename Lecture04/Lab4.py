# Donovan McKinney
# Python
# Mod 4 Lab 4 
# 2/13/2024 

from helper import get_int

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def __str__(self) -> str:
        return f"{self.year} | {self.make} {self.model}"
    

vehicles = [
    Vehicle("Nissan", "Sentra", 2002), 
    Vehicle("Ford", "f150", 2020), 
    Vehicle("Honda", "CTS", 2014)
]

def list_vehicles():
    print(f"There are {len(vehicles)} vehicles: ")
    i=0
    for v in vehicles:
        i+=1
        print(f"{i}: {v}")
        
def add_vehicle():
    make = input("Enter a make: ")
    model = input("Enter a model: ")
    year = input("Enter a year: ")
    vehicles.append(Vehicle(make, model, year))
    list_vehicles()
    
def remove_vehicle():
    list_vehicles()
    index = get_int("Which would you like to remove: ") -1
    vehicles.pop(index)
    list_vehicles()
    
while True:
    print("1. Add a vehicle")
    print("2. Remove a vehicle")
    print("3. Exit")
    choice = get_int("Selection: ")
    if choice == 1:
        add_vehicle()
    elif choice == 2:
        remove_vehicle()
    else: 
        break