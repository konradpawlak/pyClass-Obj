# composition - using classes objects as other objects parameters -> HAS-A relationship
# do this instead of inheritance -> IS-A relationship like 
# composition better than inhertiance - design choice

class World:
    def __init__(self, name, population, gym): # innit function is always doing the same thing assign parameters(passed to class) to the attributes(inside class) with the same name
        self.name = name
        self.population = population
        self.gym = gym

    def __repr__(self):
        return f"World(name={repr(self.name)}, population={repr(self.population)}, gym={repr(self.gym)})"
    
class Trainer:
    def __init__(self, name, age, pokis, world):
        self.name = name
        self.age = age
        self.pokis = pokis
        self.world = world

p = World("Kanto", 2577, "Veridian City")
e = Trainer("Matt", 19, 4, p)
print(
    "Trainer data:\n"
    "...\n"
    "name: " + str(e.name) + "\n"
    "age: " + str(e.age) + "\n"
    "pokemons: " + str(e.pokis) + "\n"
    "location: " + str(e.world.name) + "\n"
    "...file closed!\n"
    )

print(e.__dict__)