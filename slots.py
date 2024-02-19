class Developer:
    def __init__(self, name, age, salary, framework):
        self.name = name
        self.age = age
        self.salary = salary
        self.framework = framework

class Tester:
    __slots__ = ("name", "age", "salary", "framework") # have to be iterables with all names of atributes, or use tuple for example :)

    def __init__(self, name, age, salary, framework):
        self.name = name
        self.age = age
        self.salary = salary
        self.framework = framework

class JuniorTester(Tester):
    __slots__ = ("quiz", "WyzyskWLabie") # subclass need only to add slots for params that are out of superclass scope
    pass


employee1 = Developer("Relu", 49, 1100, "Flask")
employee2 = Tester("Pikr", 94, 1600, "Django")

print(employee1.__dict__)
#print(employee2.__dict__)

#print(employee1.__slots__)
print(employee2.__slots__)

# slots provide faster access and memory
# tradeof: you cannot add attributes dynamicaly. they are static now.