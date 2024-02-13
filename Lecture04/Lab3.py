# Donovan McKinney
# Python
# Mod 4 Lab 3
# 2/13/2024 

from helper import get_int

class GroceryItem:
    def __init__(self, name, category, quantity):
        self.name = name
        self.category = category
        self.quantity = quantity
        
    def __str__(self):
        return f"{self.name} - {self.category}: {self.quantity}"
    
items = [
    GroceryItem("Ruffle", "Chips", 3),
    GroceryItem("Bacon", "Meat", 1),
    GroceryItem("Ice Cream", "Dairy", 2), 
    GroceryItem("Coke", "Drink", 12)
]

def list_item():
    i = 0
    for item in items:
        print(f"Item {i + 1}: {item}")
        i += 1
        
def update_item():
    list_item()
    index = get_int(f"\tWhat item would you like to update: ") -1
    items[index].quantity =get_int(f"How many {items[index].name} do you want: ")
    list_item()
    
while True:
    print(f"\n1. List items\n2. Update an item\n3. Exit")
    choice = get_int(f"\nSelection: ")
    if choice == 1:
        list_item()
    elif choice == 2:
        update_item()
    else:
        break