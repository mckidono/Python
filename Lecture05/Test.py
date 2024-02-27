jobs_descriptions = {
    "Account Manager": "Responsible for making sure client and customer needs are being met and understood by each department in the company", 
    "Project Manager": "Lead and guide the work of technical staff. Serve as liaison between business and technical aspects of projects. Plan project stages and assess business implications for each stage.", 
    "Senior Developer": "Responsible for overseeing junior developers on projects and supporting various development duties", 
    "Junior Developer": "Your primary focus will be to learn the codebase, gather user data, and respond to requests from senior developers"
}

class Employee:
    def __init__(self, first_name, last_name, email, job, username):
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
        
    
Employees = []

def list_employees():
    for sh in Employees:
        print(sh)
        
def add_employee():
    first_name = input("Enter First name: ")
    last_name = input("Enter Last name: ")
    username = input("Enter Username: ")
    email = input("Enter Email: ")
    job = input("Enter Job: ")
    Employees.append(Employee(first_name,last_name,username,email,job))
    
def rm_employee():
    pass # You need to implement this function

def list_jobs():
    for key, value in jobs_descriptions.items():
        print(key)

while True:
    print("\t1. List Employees")
    print("\t2. Add Employee")
    print("\t3. Remove Employee")
    print("\t4. List Jobs")
    print("\t5. Exit")
    choice = int(input("Pick a selection(1-5): ")) 
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