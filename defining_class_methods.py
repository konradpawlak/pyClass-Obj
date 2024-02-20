# instance method/function -> becouse all methods inside a class will receive an isntance as a first parametr SELF.
# what if i need a method that works with class but doesnt need to work with isntances of that class?
# i need a class method instead of isntnace method
#


class PokemonTrainer:
    minimum_pokemons = 2
    maximum_pokemons = 6

    @classmethod
    def change_minimum_pokemons(cls, update_minimum):
        if update_minimum > 4:
            raise ValueError('Minimum number cannt be higher than half bro...')
        else:
            cls.minimum_pokemons = update_minimum # code is dynamic thanks to this | chanching name of the class in the future prevents failing method here

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

print(PokemonTrainer.minimum_pokemons)
PokemonTrainer.change_minimum_pokemons(3)
print(PokemonTrainer.minimum_pokemons)