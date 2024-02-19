# inheritance helps with DRY
# be create BASE CLASS(parent) with DEIVED CLASSES(child) from it.
# from latin -> SUPERCLASS - above something -> SUBCLASSES
# in simple: CLASSES INHERIT CODE FROM OTHER CLASSES

# superclass:

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
        self.salary += self.salary * (percent/100)
        self.salary += bonus

# method will always look first for the function in the class, id its not therr it will search outside
# to override superclass method we have to name it the same in the subclasses



# every class inherits. empty class inherits from python object class
# ex. 

class Customer(object):
    pass

# object is superclass of all classes


employee1 = Tester("Lauren", 29, 1050)
employee2 = Developer("Robert", 34, 1500)
employee3 = Developer("Tofel", 34, 1500)
employee4 = Customer()

print(isinstance(employee1, Tester))
print(isinstance(employee2, Developer))
print(isinstance(employee3, Developer))
print(isinstance(employee4, Customer))

# polimorfism here: if you only use basic functions from supercalss, it doesnt
# matter from which sublass objects are created. Tester or developer
# could be used as employees objects

print(issubclass(Developer, Employee))
print(issubclass(Tester, Employee))
print(issubclass(Employee, object))
print(issubclass(Developer, object))
print(issubclass(Tester, object))
print(issubclass(Customer ,object))

# best example of inheritance is EXCEPTION, every exception is child of base(BaseException) exception
# if you want your own exception, just create them ingertiancing from Except exception class that already exists.

print(employee1.salary)
print(employee2.salary)
print(employee3.salary)


employee1.increase_salary(15)
employee2.increase_salary(20)
employee3.increase_salary(20, 500)


print(employee1.salary)
print(employee2.salary)
print(employee3.salary)

employee1.run_tests()


print(isinstance(employee1))

# try??

try:
    # something that raises the FloatingPointError or the ZeroDivisionError
    raise FloatingPointError("Watch out, a floating point error!")
except ArithmeticError as e: # instead of focusing on diff errors, just catch all arithmetic ones, Aritmethic is superclass of floatingpoint and zerodivision
    # handle this error
    print(e)