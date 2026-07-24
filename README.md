# Employee Management System (OOP Project)

## 📌 Project Overview

The **Employee Management System** is a Python console-based application developed using **Object-Oriented Programming (OOP)** concepts. It allows users to create, manage, update, display, and delete employee records while demonstrating important OOP principles such as:

* Encapsulation
* Inheritance
* Polymorphism
* Method Overriding
* Method Overloading
* Constructor Usage
* Class Variables
* Getters and Setters
* Destructor
* `isinstance()`
* `issubclass()`

This project is ideal for beginners who want to understand how OOP concepts are applied in real-world applications.

---

## 🚀 Features

### Employee Management

* Add new employees
* Display employee details
* Update employee information
* Delete employee records

### Role Management

* Manager Role
* Developer Role

### OOP Concepts Demonstrated

* Encapsulation using private attributes
* Inheritance (`Manager` and `Developer` inherit from `Employee`)
* Runtime Polymorphism
* Method Overriding
* Getters and Setters
* Class Variables
* Destructor
* `isinstance()` function
* `issubclass()` function

---

## 📂 Project Structure

```text
Employee Management System
│
├── Employee Class
│   ├── Private Employee ID
│   ├── Private Salary
│   ├── Getters & Setters
│   ├── Display Method
│   └── Role Method
│
├── Manager Class
│   ├── Department
│   ├── Overridden Display Method
│   └── Overridden Role Method
│
├── Developer Class
│   ├── Programming Language
│   ├── Overridden Display Method
│   └── Overridden Role Method
│
├── Employee Storage (List)
│
├── Functions
│   ├── add_employee()
│   ├── show_employees()
│   ├── update_employee()
│   ├── delete_employee()
│   ├── inheritance_check()
│   └── total_objects()
│
└── Main Menu
```

---

## 🛠 Technologies Used

* Python 3.x
* Object-Oriented Programming (OOP)

---

## 📖 OOP Concepts Used

### 1. Encapsulation

Private attributes:

```python
self.__employee_id
self.__salary
```

Accessed through Getter and Setter methods.

---

### 2. Inheritance

```python
class Manager(Employee):
```

```python
class Developer(Employee):
```

Both classes inherit from the Employee class.

---

### 3. Polymorphism

```python
emp.role()
```

Different output depending on whether the object is Manager or Developer.

---

### 4. Method Overriding

```python
def display(self):
```

Manager and Developer classes override the display method of Employee.

---

### 5. Class Variable

```python
total_employees = 0
```

Tracks the total number of employee objects created.

---

### 6. isinstance()

```python
isinstance(emp, Employee)
```

Checks whether an object belongs to the Employee class.

---

### 7. issubclass()

```python
issubclass(Manager, Employee)
```

Checks inheritance relationships.

---

## 📸 Sample Output

```text
========== EMPLOYEE MANAGEMENT SYSTEM (OOP PROJECT) ==========

Select an Option:

1. Create Employee
2. Show Details
3. Update Employee
4. Delete Employee
5. Check issubclass
6. Total Number of Employee
7. Exit
```

### Adding a Manager

```text
Enter Employee ID : E101
Enter Name : Dharmendra
Enter Age : 22
Enter Salary : 50000

Tracking Roles:
1. Manager
2. Developer

Select Role : 1
Enter Department : HR

Employee Added Successfully!
```

### Display Output

```text
Manager Details:

Employee ID : E101
Name        : Dharmendra
Age         : 22
Salary      : 50000
Department  : HR

Role : Manager
Is Employee Object : True
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/your-username/employee-management-system.git
```

### Navigate to Project Folder

```bash
cd employee-management-system
```

### Run the Program

```bash
python employee_management.py
```

---

## 🎯 Learning Outcomes

After completing this project, you will understand:

* Python Classes and Objects
* Constructors and Destructors
* Encapsulation
* Inheritance
* Polymorphism
* Method Overriding
* Getters and Setters
* Runtime Object Handling
* CRUD Operations using Python Lists

---

## 🔮 Future Improvements

* File Handling Support
* JSON Data Storage
* SQLite Database Integration
* Search Employee Feature
* Employee Login System
* GUI using Tkinter
* Web Version using Flask/Django

---

## 👨‍💻 Author

**Dharmendra Rajput**

BCA Graduate | Python Developer | Aspiring Data Analyst

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub and sharing it with others.

Happy Coding! 🚀
