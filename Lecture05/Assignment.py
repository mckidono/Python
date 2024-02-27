# Donovan McKinney
# Python
# Mod 5 Lab 4 
# 2/20/2024 
from helper import get_letter, get_email, get_int_in_range


#   Remove Employee
# Validate the following
#   First and last name, letters only


jobs_descriptions = {
    "Account Manager": "Responsible for making sure client and customer needs are being met and understood by each department in the company", 
    "Project Manager": "Lead and guide the work of technical staff. Serve as liaison between business and technical aspects of projects. Plan project stages and assess business implications for each stage.", 
    "Senior Developer": "Responsible for overseeing junior developers on projects and supporting various development duties", 
    "Junior Developer": "Your primary focus will be to learn the codebase, gather user data, and respond to requests from senior developers"
}

#https://www.indeed.com/hire/job-description/account-manager
#https://www.onetonline.org/link/summary/15-1299.09
#https://www.betterteam.com/senior-developer-job-description
#https://www.betterteam.com/junior-software-developer-job-description
 
class Employee:
    def __init__(self, first_name, last_name, username, email, job):
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.email=email
        self.job=job
        
    def __str__(self):
        return(f'{self.last_name}, {self.first_name} | {self.username} | {self.job} | {self.email}\n\t{self.get_job_desc()}')
    
    def get_job_desc(self):
        if self.job in jobs_descriptions:
            return jobs_descriptions[self.job]
        else:
            return f"{self.job} does not have a definition"
        
    
Employees = [
    Employee("Isecc", "Juarez", "ijuarez", "ijuarez@agency.com", "Account Manager"),
    Employee("Aaron", "Qeantinar", "aqeantinar" , "aqeantinar@agency.com", "Project Manager"),
    Employee("Donovan", "McKinney", "dmckinney", "dmckinney@agency.com", "Senior Developer")
]

def list_employees():
    for em in Employees:
        print(em)
        
def add_employee():
    first_name = get_letter("First name: ")
    last_name = get_letter("Last name: ")
    username = get_letter("Username: ")
    email = get_email("Email: ")
    job = input("job: ")
    Employees.append(Employees(first_name,last_name,username,email,job))
    
def rm_employee():
    list_employees()
    username = input("Enter the username of the employee you want to remove: ")
    for employee in Employees:
        if employee.username == username:
            Employees.remove(employee)
            print(f"{employee.first_name} {employee.last_name} has been removed.")
            return
    print("Employee not found.")

def list_jobs():
    for key, value in jobs_descriptions.items():
        print(key)
    
while True:
    print("\t1. List Employees")
    print("\t2. Add Employee")
    print("\t3. Remove Employee")
    print("\t4. List Jobs")
    print("\t5. Exit")
    choice = get_int_in_range("Pick a selection(1-5)", 1, 5) 
    if choice == 1:
        list_employees()
    elif choice == 2:
        add_employee()
    elif choice == 3:
        rm_employee()
    elif choice == 4:
        list_jobs()
    else:
        break