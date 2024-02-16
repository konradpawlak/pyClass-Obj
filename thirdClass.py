import datetime

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
    
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def __str__(self): # dodawanie tego str tutaj zmienia defaultowy print objektu -> print(employee1) np z <__main__.Employee object at 0x0000025EBE43EF50> na text ustawiony // DO TEGO TO LOCAL SCOPE STR() jest global scopem
       return(f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}") 
    
    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)}, "
            f"{repr(self.position)}, {repr(self.salary)})"
        )

employee1 = Employee("Ji-Soon", 28, "developer", 1800) # emplyee instances not an objects - instanciated - initiated new employees instances
employee2 = Employee("Jason", 38, "tester", 1050) # object is an broad therm really
employee3 = Employee("Rylle", 33, "tech-lead", 1450) # object is an broad therm really

dt = datetime.date(2024, 1, 12)

user_input = int(input("Input salary: "))
if user_input < 1000:
    raise ValueError('Minimum wage is $1000')
else:
    employee3.salary = user_input

print(dt)
print(repr(dt))
print(str(dt))

print(str(employee1))
print(repr(employee1))
print(eval(repr(employee1)))