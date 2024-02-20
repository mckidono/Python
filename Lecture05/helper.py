def get_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            return val
        except ValueError:
            print("Please enter a valid number")
            
