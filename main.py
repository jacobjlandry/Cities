# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Models.City import City
from Models.NPC import NPC

def makeCity(name):
    npc = NPC("Jacob", "", "Landry", "barbarian")
    print(npc.getName)
    print(npc.getOccupation().name)
    print(npc.getWealth())
    print(npc.getIncome())
    print("=================")

    city = City(name, 'small')

    print(city.getName())
    print("=================")
    print(city.getSize())
    print(city.getPopulation())

    # force some items, our adventurers made an impact
    #city.threatLevel = 10
    #city.safetyLevel = 90

    print(city.getSafety())
    print(city.getThreat())

    print("")
    print("=================")
    print("365 Days Later")
    print("=================")
    print("")

    city.passDays(365)
    print(city.getSize())
    print(city.getPopulation())
    print(city.getSafety())
    print(city.getThreat())

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    makeCity('Winthrop')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
