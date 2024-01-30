# Donovan McKinney
# Python
# Mod 1 Lab 3
# 1/24/2024



#A = Accrued amount (principal + interest)

principal = float(    input("Initial Amount: $")  )
#P = Principal amount

interest_rate = float(    input("Interest Rate: %")   )
interest_rate = interest_rate / 100.0
#r = Annual nominal interest rate as a decimal

n = float(   input("Number of times interest is applied per year: ") )
#n = number of compounding periods per unit of time

time = float(   input("How many years have elapsed: "))
#t = time in decimal years; e.g., 6 months is calculated as 0.5 years. Divide your partial year number of months by 12 to get the decimal years.

accured_amount = round(principal * (1+ interest_rate / n) ** (n * time), 21)
#A = P(1 + r/n)nt

print(accured_amount)