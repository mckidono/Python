import re
def get_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            return val
        except ValueError:
            print("Please enter a valid number")
            
def get_int_in_range(prompt, min, max):
    while True:
        try:
            user_num = int(input(prompt))
            if user_num <= max and user_num >= min:
                return user_num
            else:
                print(f"Please enter a number between {min} and {max}")
        except:
            print("Please enter a whole number.")
            
def get_email(prompt):
    while True:
        email = input(prompt)  
        is_match = re.search(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", email)
        if is_match:
            return email
        else:
            print("Please enter a valid email")
            
def get_letter(prompt):
    while True:
        user_input = input(prompt)
        is_match = re.search("^[a-zA-Z]{1,}$", user_input)
        if is_match:
            return user_input
        else:
            print("Please enter only letters")
        