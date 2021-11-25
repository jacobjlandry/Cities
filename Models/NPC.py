import random
from Traits.Classes.Thief import Thief
from Traits.Classes.Barbarian import Barbarian
from traits.api import Delegate, Instance

class NPC:
    first_name = ""
    last_name = ""
    middle_name = ""

    # obviously we have to make this dynamic but lets see if it'll even work
    income = Delegate( 'occupation' )
    wealth = Delegate ( 'occupation' )

    # this could come from class/race traits
    hitpoints = 100
    current_hitpoints = 100
    stamina = 100
    current_stamina = 100

    # state
    dead = 0
    alive = 1

    damage = 0

    def __init__(self, first_name, middle_name, last_name, character_class):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

        if(character_class == "thief"):
            print("thief")
            self.occupation = Thief()
        elif (character_class == "barbarian"):
            print("barb")
            self.occupation = Barbarian()

    def getName(self):
        if(self.middle_name):
            return self.first_name + " " + self.middle_name + " " + self.last_name
        else:
            return self.first_name + " " + self.last_name

    def setOccupation(self, occupation):
        # set occupation string
        self.occupation = occupation

        # set income and wealth randomly, though this should depend on other factors
        # this should take into account population of the city and trade
        # examples:
        # a blacksmith in a populated but heavily guarded city might make very little
        # a blacksmight in a  populated but not guarded city might be more profitable
        # a thief in a small town might barely survive
        # a good thief in a city might do very well
        # a shopkeeper in a small town might make a decent wage with no competition
        # a shopkeeper in a large city would be largely dependent on goods and location
        #
        # for now we are just going to randomize this but there's a lot of logic to consider in the (near) future
        self.income = random.randint(1,250)
        self.wealth = random.randint(100, 3500)

    def getOccupation(self):
        return self.occupation

    def getWealth(self):
        return self.getOccupation().wealth

    def getIncome(self):
        return self.getOccupation().income

    def setHitpoints(self, hitpoints):
        self.hitpoints = hitpoints

    def getHitpoints(self):
        return self.hitpoints

    def getCurrentHitpoints(self):
        return self.current_hitpoints

    def getHealth(self):
        return self.getCurrentHitpoints()

    def hit(self, damage):
        self.current_hitpoints -= damage
        if(self.checkAlive() == 0):
            self.dead = 1
            self.alive = 0
    def takeHit(self, damage):
        self.hit(damage)
    def takeDamage(self, damage):
        self.hit(damage)

    def checkAlive(self):
        return self.current_hitpoints > 0

    def setDamage(self, damage):
        self.damage = damage

    def getDamage(self):
        return self.damage
    def blow(self):
        return self.getDamage()
    def crit(self):
        return self.getDamage * 100;