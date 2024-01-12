class Emlpoyee:
    pass

e = Emlpoyee()
print(e.__dict__)
print(type(e))
print(type(e.__dict__))
print(type(e.__class__))

class Emlpoyee1:
    def __init__(self):
        self.__dict__["name"] = "Ji-Soo"
        self.__dict__["age"] = 38
        self.__dict__["position"] = "developer"
        self.__dict__["salary"] = 1200

e1 = Emlpoyee1()
print(e1.__dict__)
print(e1)
print(e1.__class__)

class Emlpoyee2:
    def __init__(self):
        self.name = "Ji-Soo"
        self.age = 38
        self.position = "developer"
        self.salary = 1200


e2 = Emlpoyee2()
print(e2.name, e2.age, e2.position, e2.salary)
print(e2)
print(e2.__class__)