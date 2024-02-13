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

x = 0
for x in items:
    print(items(1))
    x += 1