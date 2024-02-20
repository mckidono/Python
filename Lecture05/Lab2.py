# Donovan McKinney
# Python
# Mod 5 Lab 2 
# 2/20/2024 

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
        
list_flags()