# this module shows pillars
# 1st pillar: ABSTRACTION - user should only see interface. Implementation is stays hidden(only class creator sees it). Ex. user of employee class should only see what attributes and methods are available. 
# Example: user should only be able to use setter function. Validation and raise error should be hidden. 
# 2nd pillar: ENCAPSULATION - 2 obcejtives: 1) class should be able to create instance group up / encapsulate related data should be in one logical unit. 
# 2) conecpt of data hiding. Data hiding relates to the idea of abstraction. Dh should be responsibilty of class?
# self.salary should be only able for the internal use inside of the class. 
# access from outside should be by getters/setters.
# python doesnt have access modifiers - public/private
# trust users xDDD
# special/private attributes are started with underscore -> self._salary
# its just a convention
# non-public attributes -> _xyz 
# 
# another option is Name mangling - can be achieved by two underscores __salary -> naming attribute error
# real name will be _Emloyee__salary !

import datetime

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary # becouse of properties we are getting validation and abstraction from real salary attribute
    
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
    
    @property # class decorator - turn regular function into property - PROPRTY DECORATOR
    def salary(self):
        return self._salary

    def get_salary(self):
        # return f"${self.salary}"
        # return round{self.salary, 2}
        # logging.info("Someone accessed th salary attribute.")
        return self._salary # DAJEMY UNDERSCORE I NIE MOZNA ZMIENIAC TEGO ATRYBUTU SPOZA KLASY
    
    # PORPERTY NAME SHOULD MATCH .SETTER NAME OF FUNCTION AND ATTRIBUTE

    @salary.setter # decoartor first take function and dot keyword setter
    def salary(self, salary): # name should match attribute
        if salary < 1000:
            raise ValueError('Minimum wage is at leat $1000 these days broo...')
        self._salary = salary

employee1 = Employee("Ji-Soon", 28, "developer", 1800) # emplyee instances not an objects - instanciated - initiated new employees instances
employee2 = Employee("Jason", 38, "tester", 1050) # object is an broad therm really
employee3 = Employee("Rylle", 33, "tech-lead", 1450) # object is an broad therm really

dt = datetime.date(2024, 1, 12)

print(dt)
print(repr(dt))
print(str(dt))

print(str(employee1))
print(repr(employee1))
print(eval(repr(employee1)))

print(employee3.salary)
employee3.salary = 2000
print(employee3.salary)

# PROPERTIES PRIVE ABSTRACTION, SO USERS DONT HAVE TO CALL SETTERS/GETTERS