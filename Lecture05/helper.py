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