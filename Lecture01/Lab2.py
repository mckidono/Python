# Donovan McKinney
# Python
# Mod 1 Lab 2
# 1/24/2024

a  = int(   input("Enter a number for a: ") )
b  = int(   input("Enter a number for a: ") )
print(f"The value of a is {a} and the value of b is {b}")
print()

print("Sum: " + str((a + b)))
print("Difference: " + str((a - b)))
print("Product: " + str((a * b)))
print("Quotient: " + str((a / b)))
print("Remainder: " + str((a % b)))
print("Power: " + str((a ** b)))
print("Floor Quotient: " + str((a // b)))
print()

#(a)b-a
print("(a)b-a: " + str(a * b - a) )
#a(b-a)
print("a(b-a): " + str(a * ( b - a )) )
#(a+b)^2
print("(a+b)^2: " + str( ( a + b ) ** 2 ) )
#(a+b)(a^2) 
print("(a+b)(a^2): " + str( ( a + b ) * ( a ** 2 ) ) )
#(a + b^2) / (a - b) 
print("(a + b^2) / (a - b): " + str( (a + b ** 2) / ( a - b ) ) )