# Donovan McKinney
# Python
# Mod 1 Assignment
# 1/24/2024

p = int(    input("What is the Loan Amount: ")  )
# p = Principal Loan Amount

r = float(    input("What is the Interest rate: ")    )
r = (r/100)/12
# r = Interest Rate

n = int(    input("How many payments(Year): ")    )
n = n * 12
# n = Number of Payments


M = round(p * ( (r * ((1 + r) ** n) ) / (((1 + r) ** n) - 1) ) , 2)
# M = Monthly Payment

print("Your monthly payment is " + str(M))
