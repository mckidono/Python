# Donovan McKinney
# Python
# Mod 5 Lab 1 
# 2/20/2024 

#dictionaries hold key value pairs

counties_population = {
    "Milwaukee": 939123, 
    "Dane": 555474, 
    "Waukesha": 404332, 
    "Brown": 267365,
    "Racine": 197379
}

print( counties_population["Milwaukee"])

counties_population["Milwaukee"] = 1000000

counties_population["Outagamie"] = 189620

counties_population.pop("Racine")

for county, population in counties_population.items():
    print(f'{county} county | population: {population}')