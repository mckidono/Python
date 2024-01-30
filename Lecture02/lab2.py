# Donovan McKinney
# Python
# Mod 2 Lab 2
# 1/31/2024

def calc_change(amount):
    
    print(f"Change for {amount}")
    
    dollars = amount // 1
    amount = round(amount % 1,2)
    
    quarters = amount // 0.25
    amount = round(amount % 0.25,2)
    
    dime = amount // 0.10
    amount = round(amount % 0.10,2)
    
    nickel = amount // 0.05
    amount = round(amount % 0.05,2)
    
    penny = amount / 0.01
    amount = amount % 0.01,2
    
    if dollars > 0:
        print(str(round(dollars)) + " dollar bill(s)")
    if quarters > 0:
        print(str(round(quarters)) + " quarter(s)")
    if dime > 0:
        print(str(round(dime)) + " dime(s)")
    if nickel > 0:
        print(str(round(nickel)) + " nickel(s)")
    if penny > 0:
        print(str(round(penny)) + " penny(s)")
    
amount = float(input("Enter an amount of money: "))
calc_change(amount)
    