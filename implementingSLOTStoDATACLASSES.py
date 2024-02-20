from dataclasses import dataclass
from typing import Any

@dataclass(slots=True) # <- very simple to add slots
class World:
    name: Any
    payment: Any
    client: Any

    def notify_gym(self): # easy way adding methods. siple usage of attributes
        print(f"Notifying the gym about incoming trainer! Hes name is {self.name}...!")
    
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