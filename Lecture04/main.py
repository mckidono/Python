#Create a Class based around your interest
#   Include three properties
#   Include an init and str method
#Prepopulate a list of your chosen items with three items
#Create a menu for your application that does the following
#   Adds and item with based on user input for the properties
#   Removes an item chosen by the user
#   Updates one of the properties based on user input

class Game:
    def __init__(self, name, genre, year):
        self.genre = genre
        self.name = name
        self.year = year
        
    def __str__(self) -> str:
        return f"{self.year} | {self.name} {self.genre}"
    
    def update_game_property(self, property_name, new_value):
        if hasattr(self, property_name):
            setattr(self, property_name, new_value)
            list_games()
    

games = [
    Game("HELLDIVERS 2", "PVE", 2024), 
    Game("League of Legends", "MOBA", 2009), 
    Game("Risk of Rain 2", "Rougelite", 2019)
]

def list_games():
    print(f"There are {len(games)} games: ")
    i=0
    for v in games:
        i+=1
        print(f"{i}: {v}")
        
def add_game():
    name = input("Enter a name: ")
    genre = input("Enter a genre: ")
    year = input("Enter a year: ")
    games.append(Game(name, genre, year))
    list_games()
    
def remove_game():
    list_games()
    index = int(input("Which would you like to remove: ")) -1
    games.pop(index)
    list_games()
    
def update_game():
    list_games()
    index = int(input("Which game would you like to update: ")) - 1
    game = games[index]
    property_name = input("Enter the property name you want to update (name, genre, year): ")
    new_value = input(f"Enter the new value for {property_name}: ")
    game.update_game_property(property_name, new_value)
    list_games()
    
while True:
    print("1. Add a game")
    print("2. Remove a game")
    print("3.Update a Game")
    print("3. Exit")
    choice = int(input("Selection: "))
    if choice == 1:
        add_game()
    elif choice == 2:
        remove_game()
    elif choice == 3:
        update_game()
    else: 
        break