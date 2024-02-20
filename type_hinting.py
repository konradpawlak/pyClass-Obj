# type hinting
# my-py is good addon from pip to check consistencies of types

from dataclasses import dataclass
from typing import Any

@dataclass
class World:
    name: Any
    payment: Any
    client: Any
    
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

# you run it from terminal by: $ mypy classes.py