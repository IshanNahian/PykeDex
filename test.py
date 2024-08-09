import random
from pokemon import Pokemon

test = Pokemon(1, 1, "arceus")
test.chosen(216, 287, 480, 329)
print(test.is_mythical)