# the anti-pattern
# sometimes we use concept of 'traits'. that way we can add additional functionality to he class without actually using multiple inhertinaces.
# Mixin-classes - very sepcial

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

class SlotsInspectorMixin:
    def has_slots(self):
        return hasattr(self, "__slots__")

class JuniorDev(SlotsInspectorMixin, Developer):
    __slots__ = ("code_review",)

    pass


employee1 = Developer("Relu", 49, 1100, "Flask")
employee2 = Tester("Pikr", 94, 1600, "Django")
employee3 = JuniorDev("Nikto", 55, 1300, "Flask")

print(employee3.has_slots())

# METHOD RESOLUTION ORDER

print(JuniorDev.__mro__)
print(employee3.__dict__)
print(employee1.__dict__)
