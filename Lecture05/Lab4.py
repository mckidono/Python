# Donovan McKinney
# Python
# Mod 5 Lab 4 
# 2/20/2024 

roles_descriptions = {
    "Administrator": "Duties relate to the functions of the college and supporting students outside of the classroom",
    "Instructor": "Support students through creation and execution of lesson plans",
    "Student": "Attend classes and complete coursework to earn a degree"
}

class Stakeholder:
    def __init__(self, first_name, last_name, email, role):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.role=role
        
    def __str__(self):
        return(f'{self.last_name}, {self.first_name} | {self.role} | {self.email}\n\t{self.get_role_desc()}')
    
    def get_role_desc(self):
        if self.role in roles_descriptions:
            return roles_descriptions[self.role]
        else:
            return f"{self.role} does not have a definition"
        
    
Stakeholders = [
    Stakeholder("Rich", "Barnhouse", "rbarn@wctc.edu", "Administrator"),
    Stakeholder("Patrick", "Gerber", "pgerber1@wctc.edu", "Instructor"),
    Stakeholder("Donovan", "McKinney", "dmckinney7@my.wctc.edu", "Student")
]

def list_stakeholders():
    for sh in Stakeholders:
        print(sh)
        
