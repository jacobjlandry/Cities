from traits.api import HasTraits
import random

class Thief( HasTraits ):
    name = "Thief"
    income = random.randint(100,2500)
    wealth = random.randint(0,500)