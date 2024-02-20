# classes and fucntions are object in python. 
# its not true for compiling languages like c++
# its just a code, where fucntion is compiled to instructions 01010100 and classes use no memory if not created objects
# if python sees function or class it will already take memory space for it
# function is an instance of function class and function name is identifier of it in memory
# a class is an instance of class type and the name is identifier...
# 

class PokemonTrainer:
    minimum_pokemons = 2
    maximum_pokemons = 6

    def __init__(self, name, age, q_pokes):
        self.name = name
        self.age = age
        self.q_pokes = q_pokes

    def increase_pokemons_count(self, number1):
        self.q_pokes = self.q_pokes + number1
    
    @property
    def q_pokes(self):
        return self._q_pokes
    
    @q_pokes.setter
    def q_pokes(self, q_pokes):
        if q_pokes < PokemonTrainer.minimum_pokemons:
            raise ValueError(f'Minimum number of pokis is {PokemonTrainer.minimum_pokemons}')
        elif q_pokes > PokemonTrainer.maximum_pokemons:
            raise ValueError(f'Maximum number of pokis is {PokemonTrainer.maximum_pokemons}')
        else:
            self._q_pokes = q_pokes

print(PokemonTrainer.__dict__)
print(PokemonTrainer.minimum_pokemons)
print(PokemonTrainer.maximum_pokemons)

e = PokemonTrainer("Bug-catcher Matt", 16, 2)

print(e.q_pokes)
PokemonTrainer.__dict__["increase_pokemons_count"](e, 1)
print(e.q_pokes)
