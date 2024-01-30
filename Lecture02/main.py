# Donovan McKinney
# Python
# Mod 2 Assignment 
# 1/31/2024


print("=== Budget Calculator ===\n")


# Create a function called get_cost
#   This function should accept one parameter for the name of a cost (i.e. get_cost("rent") )
#   This function should first check if the user pays for this cost (see example)
#       If the user does pay for the cost, return the amount of the cost
#       If the user does not pay for the cost, return 0
def get_cost(rent):
    
    #checking
    pays = input("\nDo you pay for "+ rent +" (y/n): ")
    if pays == "y" or pays == "Y":
        return float( input("       How much is/are "+ rent+" per month: $"))
        
    else:
        return 0
    
        
    
            
        
# Create a function called print_report
#   This function should accept two parameters: monthly_income and monthly_costs
#   This function should output the monthly income and costs
#   This function should look if the budget is a surplus, breaks even, or is a deficit, and output a corresponding message
#   No return value is needed
def print_report(monthly_income, monthly_costs):
    print("\nMonthly Income: $" + str(monthly_income))
    print("Monthly Costs: $" + str(monthly_costs))
    if monthly_income < monthly_costs:
        deficit = round(monthly_costs - monthly_income, 2)
        print("\nYou are running a deficit of $" + str(deficit))
        
    
    elif monthly_income > monthly_costs:
        surplus = round(monthly_income - monthly_costs, 2)
        print("\nYour are running a surplus of $" + str(surplus))
        
    else:
        print("\nYou are breaking even")



# Get the following from the user
#   Pay periods per month
#   Amount of pay per pay period
pay_periods_per_month = float(input("How many times are you paid each month: "))
amount_of_pay_per_pay_period = float(input("How much is each paycheck (post-tax): $"))
monthly_income=pay_periods_per_month*amount_of_pay_per_pay_period


# Calculate the monthly cost by calling the get_cost function three times using the following arguments:
#   rent
#   groceries
#   a car

costs = ["rent","groceries","car"]
for x in costs:
    if x == 'rent':
        rent = get_cost(x)
    elif x == 'groceries':
        groceries = get_cost(x)
    elif x == 'car':
        car = get_cost(x)
monthly_costs=rent+groceries+car


# Run the print_report function
print_report(monthly_income, monthly_costs)

# Create only the functions that are described