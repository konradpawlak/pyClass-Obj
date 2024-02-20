from dataclasses import dataclass

@dataclass # <- data class decorator. makes dataclass from class
class World: # this creates innit in the background with repr function
    name: str # this is a type hint
    payment: int
    client: str
    
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