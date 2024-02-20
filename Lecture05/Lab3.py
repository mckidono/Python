# Donovan McKinney
# Python
# Mod 5 Lab 3
# 2/20/2024 

import re
from helper import get_email

user_input = input("fire od more letters: ")

is_match = re.search("^[a-zA-Z]{5, }$", user_input)

if is_match:
    print(f'{user_input} is a match')
else:
    print(f'{user_input} is not a match')
    
user_input = input("Enter  4-6 lowercase letters followed by 2 number")

is_match = re.search("^[a-z]{4,6}[0-9]{2}$", user_input)

if is_match:
    print(f'{user_input} is a match')
else:
    print(f'{user_input} is not a match')
  
get_email("Enter a valid email: ")