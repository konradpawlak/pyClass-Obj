class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

class Tester(Employee):
    def run_tests(self):
        print(f"Testing triggered by {self.name}....")
        print(f"Tests ongoing....")
        print(f"50%....")
        print(f"75%....")
        print(f"100%....")
        print(f"....Done!")

class Developer(Employee):
    def __init__(self, name, age, salary, framework): # this will be added from dev class
        super().__init__(name, age, salary) # this will be taken from superclass
        self.framework = framework 

    def increase_salary(self, percent, bonus=0):
        self.salary += self.salary * (percent/100)
        self.salary += bonus

class Developer2(Employee):
    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus


employee1 = Tester("Lauren", 29, 1050)
employee2 = Developer("Robert", 34, 1500, "flask")
employee3 = Developer2("Tofel", 34, 1500)

employee1.increase_salary(15)
employee2.increase_salary(20)
employee3.increase_salary(20, 500)

print(employee1.salary)
print(employee2.salary)
print(employee3.salary)

print(employee2.name)
print(employee2.framework)