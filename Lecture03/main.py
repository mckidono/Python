# Donovan McKinney
# Python
# Mod 3 Assignment 
# 2/12/2024


stops = []


def get_menu_option():
    return int(input("What would you like to do? (1) Add a stop, (2) List current stops, (3) Clear all stops, (4) Quit: "))
    

while True:
    user_choice = get_menu_option()
    if user_choice == 4:
        break
    elif user_choice <= 0 or user_choice >= 5:
        print("Please enter a valid menu option.")
        continue

    if user_choice == 1:
        stop_name = input("Enter the name of the stop: ")
        stops.append(stop_name)
    if user_choice == 2:
        print("Current stops: ")
        for stop in stops:
            print(stop)
    if user_choice == 3:
        stops.clear()
    if len(stops) == 0:
        print("There are no stops available.")