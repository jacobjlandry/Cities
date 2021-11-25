from traits.api import HasTraits
import random

class Barbarian( HasTraits ):
    name = "Barbarian"
    income = random.randint(10,100)
    wealth = random.randint(0,10)