# Donovan McKinney
# Python
# Mod 5 Lab 2 
# 2/20/2024 
from helper import get_int_in_range
countries_colors = {
    "Malta": ["red","white"],
    "Greece": ["blue", "white"],
    "St. Lucia" : ["blue","black", "white", "yellow"]
}

def list_flags():
    for k, v in countries_colors.items():
        print(f'\n{k} | ')
        for color in v:
            print(f'\t{color}')
        
        #print("\t" + ", ".join(v))
        
def add_flag():
    country = input("Enter the country name: ")
    colors = []
    while True:
        color = input("Enter a color (! to end): ")
        if color == "!":
            break
        
        colors.append(color)
        
    countries_colors[country] = colors
    
def get_colors_by_country(name):
    if name in countries_colors:
        print(", ".join(countries_colors[name]))
    else:
        print("That country is not in the list")
        
while True:
    print("\n")
    print("\t1.List the flags")
    print("\t2. Add a flag")
    print("\t3. Getting color by country")
    print("\t4. Exit")
    choice = get_int_in_range("\t selection: ", 1, 4)
    if choice == 1:
        list_flags() 
    elif choice == 2:
        add_flag
    elif choice == 3:
        get_colors_by_country(input("Enter a country name: "))
    else:
        break