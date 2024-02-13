# Donovan McKinney
# Python
# Mod 4 Lab 2
# 2/13/2024 

class Pet:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
        
    def __str__(self) -> str:
        return f"This {self.species} is named {self.name} and says {self.sound}"
    
    def speak(self):
        print(f"The {self.species} goes {self.sound}")
    
p1 = Pet(input("\nWhat is your pet's name: "), input("What is your pet's species: "), input("What sound does your pet make: "))
p2 = Pet(input("\nWhat is your pet's name: "), input("What is your pet's species: "), input("What sound does your pet make: "))
p3 = Pet(input("\nWhat is your pet's name: "), input("What is your pet's species: "), input("What sound does your pet make: "))

print(p1)
p1.speak()
print(p2)
p2.speak()
print(p3)
p3.speak()
