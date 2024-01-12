class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
    
    def increase_salary(self, percent): # this is an instance function / methods are functions inside class
        self.salary += self.salary * (percent/100)
    
    def employee_info(self):
      #  print(f"{employee['name']} is {employee['age']} years old. Employee is a {employee['position']} with the salary of ${employee['salary']}") this is for dict not obj
      print(f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}")

    def info(self):
      #  print(f"{employee['name']} is {employee['age']} years old. Employee is a {employee['position']} with the salary of ${employee['salary']}") this is for dict not obj
      print(f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}")

employee1 = Employee("Ji-Soon", 28, "developer", 1200) # emplyee instances not an objects - instanciated - initiated new emplyees instances
employee2 = Employee("Jason", 38, "tester", 1050) # object is an broad therm really

Employee.employee_info(employee1)
employee2.info()
employee2.increase_salary(20)
Employee.info(employee1)
employee1.info()
employee2.info()
# print(employee1.__dict__)
# print(employee2.__dict__)

# WE USE SELF COS WE CAN SKIP WRITING EMPLOYEE OR ANOTHER OBJECT INSTANCE NAME SO ITS GOOD!!!!!


"""

    def increase_salary(employee, percent): # this is an instance function / methods are functions inside class
        employee['salary'] += employee['salary'] * (percent/100)
    
    def employee_info(employee):
      #  print(f"{employee['name']} is {employee['age']} years old. Employee is a {employee['position']} with the salary of ${employee['salary']}") this is for dict not obj
      print(f"{employee.name} is {employee.age} years old. Employee is a {employee.position} with the salary of ${employee.salary}")

    def info(employee):
      #  print(f"{employee['name']} is {employee['age']} years old. Employee is a {employee['position']} with the salary of ${employee['salary']}") this is for dict not obj
      print(f"{employee.name} is {employee.age} years old. Employee is a {employee.position} with the salary of ${employee.salary}")

"""