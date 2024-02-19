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
    def increase_salary(self, percent, bonus=0):
        self.salary += self.salary * (percent/100) # i take this code /continue in line 26
        self.salary += bonus

class Developer2(Employee):
    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent) # and do this instead. super will automatically pass the self instance to the function call // also super in this case make this dynamic so the future maintenenace is easier
        # Employee.increase_salary(self, percent) this is happening in the background
        self.salary += bonus

# REMEMBER THAT SELF WILL ALWAYS CALL TO THE METHOD FROM THE SPECIFIC INSTANCE/CLASS ITS IN, NOT SUPERCLASS EVEN
        
# test if it works

employee1 = Tester("Lauren", 29, 1050)
employee2 = Developer("Robert", 34, 1500)
employee3 = Developer2("Tofel", 34, 1500)

employee1.increase_salary(15)
employee2.increase_salary(20)
employee3.increase_salary(20, 500)

print(employee1.salary)
print(employee2.salary)
print(employee3.salary)