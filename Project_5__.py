
#  =================================================
#     EMPLOYEE MANAGEMENT SYSTEM (OOP PROJECT) 
#  =================================================

class Employee:

    # Class Variable
    total_employees = 0

    # Constructor Overloading using default arguments
    def __init__(self, employee_id=0, name="", age=0, salary=0):

        # Encapsulation
        self.__employee_id = employee_id
        self.name = name
        self.age = age
        self.__salary = salary
        # total object count
        Employee.total_employees += 1

    # Getter method
    def get_employee_id(self):
        return self.__employee_id

    # Setter method
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter method
    def get_salary(self):
        return self.__salary

    # Setter method
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid Salary!")

    # Method Overloading
    def display(self,):

        print("\nEmployee Details: ")
        print("Employee ID :", self.__employee_id)
        print("Name        :", self.name)
        print("Age         :", self.age)
        print("Salary      :", self.__salary)

    # Method for Polymorphism
    def role(self):
        print("Role : Employee")

    # Destructor
    def __del__(self):
        print(f"Object Destroyed of Name: {self.name}")


# ==========================================
# Manager Class
# ==========================================

class Manager(Employee):

    def __init__(self, employee_id, name, age, salary, department):

        super().__init__(employee_id, name, age, salary)
        self.department = department

    # Method Overriding
    def display(self):

        print("\nManager Details:>>\n")
        print("Employee ID          :", self.get_employee_id())
        print("Name                 :", self.name)
        print("Age                  :", self.age)
        print("Salary               :", self.get_salary())
        print("Department           :", self.department)
         
    # Method Overriding         
    def role(self):         
        print("Role                 : Manager")


# ==========================================
# Developer Class
# ==========================================

class Developer(Employee):

    def __init__(self, employee_id, name, age, salary, language):

        super().__init__(employee_id, name, age, salary)
        self.language = language

    # Method Overriding
    def display(self):

        print("\nDeveloper Details:>>\n")
        print("Employee ID          :", self.get_employee_id())
        print("Name                 :", self.name)
        print("Age                  :", self.age)
        print("Salary               :", self.get_salary())
        print("Programming Language :", self.language)

    # Method Overriding
    def role(self):
        print("Role                 : Developer")


# ==========================================
# Employee Storage
# ==========================================

employees = []


# ==========================================
# Add Employee
# ==========================================

def add_employee():

    emp_id = input("Enter Employee ID : ")
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    salary = int(input("Enter Salary : "))
    print("\nTracking Roles: ")
    print("1. Manager")
    print("2. Developer")

    choice = input("Select Role : ")

    if choice == "1":

        dept = input("Enter Department : ")

        emp = Manager(emp_id, name, age, salary, dept)

    elif choice == "2":

        language = input("Enter Programming Language : ")

        emp = Developer(emp_id, name, age, salary, language)

    else:
        print("Invalid Choice!")
        return

    employees.append(emp)

    print("\nEmployee Added Successfully!")

    


# ==========================================
# Show Employees
# ==========================================

def show_employees():

    if len(employees) == 0:
        print("No Employee Found!")
        return

    for emp in employees:

        emp.display()

        # Run Time Polymorphism
        emp.role()

        # isinstance()
        print("Is Employee Object   :",
              isinstance(emp, Employee))

        print("-" * 35) # this make seprate line *40 time(-----like this) 


# ==========================================
# Update Employee
# ==========================================

def update_employee():

    eid = input("Enter Employee ID : ")

    for emp in employees:

        if emp.get_employee_id() == eid:

            new_name = input("Enter New Name : ")
            new_salary = float(input("Enter New Salary : "))

            emp.name = new_name
            emp.set_salary(new_salary)

            print("Employee Updated Successfully!")
            return

    print("\nEmployee Not Found!")


# ==========================================
# Delete Employee
# ==========================================

def delete_employee():

    eid = input("Enter Employee ID : ")

    for emp in employees:

        if emp.get_employee_id() == eid:

            employees.remove(emp)

            print("Employee Deleted Successfully!")
            return

    print("\nEmployee Not Found!")


# ==========================================
# Check Inheritance
# ==========================================

def inheritance_check():

    print("\nManager is subclass of Employee :",
          issubclass(Manager, Employee))

    print("Developer is subclass of Employee :",
          issubclass(Developer, Employee))


# ==========================================
# Total Objects
# ==========================================

def total_objects():

    print("\nTotal Employee : ",
          Employee.total_employees)


# ==========================================
# Main Program
# ==========================================

print("\n========== EMPLOYEE MANAGEMENT SYSTEM (OOP PROJECT) ==========\n")
while True:

    print("\nSelect an Option: ")
    print("1. Create Employee")
    print("2. Show Details")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Check issubclass")
    print("6. Total Number of Employee")
    print("7. Exit")

    ch = input("\nEnter Choice : ")

    if ch == "1":
        #function calling
        add_employee()

    elif ch == "2":
        show_employees()

    elif ch == "3":
        update_employee()

    elif ch == "4":
        delete_employee()

    elif ch == "5":
        inheritance_check()

    elif ch == "6":
        total_objects()

    elif ch == "7":
        print("\nExiting the project All resouces have been freed \n\nGoodBye!\n")
        break

    else:
        print("Invalid Choice!")